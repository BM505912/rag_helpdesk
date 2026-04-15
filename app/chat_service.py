from langchain_huggingface import HuggingFaceEmbeddings
#from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from src.file_processor import chunk_all_files
from src.chroma_db import save_to_chroma_db
from app.config import settings
from app.memory import ChatMemory

from app.gateway_client import GatewayLLMClient
from app.config import settings
from app.memory import ChatMemory
from src.file_processor import chunk_all_files
from src.chroma_db import save_to_chroma_db
from threading import Lock


memory = ChatMemory()

gateway = GatewayLLMClient(
    settings.GATEWAY_URL,
    settings.GATEWAY_API_KEY
)

db = None
db_lock = Lock()

def get_db():
    global db

    if db is None:
        with db_lock:
            # doble chequeo (patrón seguro)
            if db is None:
                print("Inicializando Chroma (una sola vez)...")
                documents = chunk_all_files()
                db = save_to_chroma_db(documents)

    return db




def build_context(question: str):
    db_instance = get_db()
    docs = db_instance.similarity_search(question, k=settings.TOP_K)

    context = "\n\n---\n\n".join(
        doc.page_content for doc in docs
    )

    return context[:settings.MAX_CONTEXT_CHARS]


def chat_stream(session_id: str, question: str):
    context = build_context(question)
    history = memory.get(session_id)

    messages = [
        {
            "role": "system",
            "content": (
                "Eres un asistente de helpdesk basado en RAG."
                "Responde buscando en el contexto."
                "Si no existe información, responde:"
                "No hay información suficiente"
               
            )
        }
    ]

    # Historial
    for msg in history:
        messages.append({
            "role": "user" if msg.type == "human" else "assistant",
            "content": msg.content
        })

    messages.append({
        "role": "user",
        "content": f"Contexto:\n{context}\n\nPregunta:\n{question}"
    })

    answer = gateway.chat(
        model=settings.MODEL_NAME,
        messages=messages
    )

    # Simulamos streaming (token por token)
    for token in answer.split():
        yield token + " "

    memory.add_user(session_id, question)
    memory.add_ai(session_id, answer)