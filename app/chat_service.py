from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from src.file_processor import chunk_all_files
from src.chroma_db import save_to_chroma_db
from app.config import settings
from app.memory import ChatMemory

memory = ChatMemory()

embedding_model = HuggingFaceEmbeddings(
    model_name=settings.EMBEDDING_MODEL
)

documents = chunk_all_files()
db = save_to_chroma_db(documents, embedding_model)

llm = ChatGroq(
    model=settings.MODEL_NAME,
    api_key=settings.GROQ_API_KEY
)

PROMPT = ChatPromptTemplate.from_messages([
    ("system", """
Eres un asistente de helpdesk basado en RAG.
Responde solo usando el contexto.
Si no existe información, responde "No hay información suficiente".
"""),
    MessagesPlaceholder(variable_name="history"),
    ("human", """
Contexto:
{context}

Pregunta:
{question}
"""),
])

def build_context(question: str):
    docs = db.similarity_search_with_score(question, k=settings.TOP_K)
    context = "\n\n---\n\n".join([doc.page_content for doc, _ in docs])
    return context

def chat_stream(session_id: str, question: str):
    # Preparar contexto
    context = build_context(question)
    history = memory.get(session_id)

    prompt = PROMPT.format(
        context=context,
        question=question,
        history=history
    )

    # Streaming
    stream = llm.stream(prompt)
    accumulated = ""

    for chunk in stream:
        token = chunk.content or ""       # token parcial
        accumulated += token
        yield token                     # <-- streaming hacia FastAPI

    # Guardar memoria luego del stream
    memory.add_user(session_id, question)
    memory.add_ai(session_id, accumulated)
