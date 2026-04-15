import os
import shutil
from langchain_chroma import Chroma
from langchain_core.documents import Document
from app.gateway_client import GatewayLLMClient
from app.config import settings
import os

#CHROMA_PATH = 'chroma'


os.environ["ANONYMIZED_TELEMETRY"] = "False"

#Recibi una list de documentos de nuestra otra funcion de file_proccessor y un embbeding model,  --Retoma una BD en Chroma
#def save_to_chroma_db(chunks: list[Document], embedding_model) -> Chroma:

    # Remove the existing Chroma database -- Si la ruta gusradad en nuestra BD existe entramos
 #   if os.path.exists(CHROMA_PATH):
        #Metemos un try algo para trabajar con carpestas y archivos de manera avanzada, se removio la BD existente
  #      try:
   #         shutil.rmtree(CHROMA_PATH)
    #    except Exception as e:
     #       print(f"Error removing Chroma database: {e}")

    # Initialize the Chroma database  --->> inicializamos BD de Chroma
    #El metodo from_documents pide 3 parametros
    # 1 - chunks
    # 2 - el directorio donde se guardara nuestra BD vectorial
    # 3 - El embedding model
   # db = Chroma.from_documents(
  #     chunks,
   #     persist_directory=CHROMA_PATH,
    #    embedding=embedding_model
   # )
    # Persist the database
    #print(f"Saved chunks to {CHROMA_PATH}")
    #return db


# ✅ Wrapper de embeddings compatible con LangChain
class GatewayEmbeddings:
    def __init__(self, client: GatewayLLMClient, model: str, dimensions: int = 512):
        self.client = client
        self.model = model
        self.dimensions = dimensions

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return [
            self.client.embeddings(
                model=self.model,
                text=text,
                dimensions=self.dimensions
            )
            for text in texts
        ]

    def embed_query(self, text: str) -> list[float]:
        return self.client.embeddings(
            model=self.model,
            text=text,
            dimensions=self.dimensions
        )


gateway = GatewayLLMClient(
    settings.GATEWAY_URL,
    settings.GATEWAY_API_KEY
)

embedding_function = GatewayEmbeddings(
    gateway,
    settings.EMBEDDING_MODEL
)




def save_to_chroma_db(chunks):
    return Chroma.from_documents(
        documents=chunks,
        persist_directory=settings.CHROMA_DIR
    )


