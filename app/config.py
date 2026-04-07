import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

class Settings:
    # Claves y modelos
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")

    # Modelo del LLM en Groq
    MODEL_NAME: str = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

    # Modelo de embeddings local
    EMBEDDING_MODEL: str = os.getenv(
        "EMBEDDING_MODEL",
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    # Cantidad de documentos a recuperar para RAG
    TOP_K: int = int(os.getenv("TOP_K", 3))

    # Configuración de la BD vectorial
    CHROMA_DIR: str = os.getenv("CHROMA_DIR", "chroma_db")

# Crear instancia global de settings
settings = Settings()

# Validaciones
if not settings.GROQ_API_KEY:
    raise RuntimeError("Falta la variable GROQ_API_KEY en el archivo .env")