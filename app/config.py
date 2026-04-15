import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

class Settings:
    # Claves y modelos
    #GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")

    # Modelo del LLM en 
    MODEL_NAME: str = os.getenv("MODEL_NAME", "gpt-4.1-mini")

    # Modelo de embeddings local
    EMBEDDING_MODEL: str = os.getenv(
        "EMBEDDING_MODEL",
        "text-embedding-3-large"
    )

    # Cantidad de documentos a recuperar para RAG
    TOP_K: int = int(os.getenv("TOP_K", 3))


    MAX_CONTEXT_CHARS = int(os.getenv("MAX_CONTEXT_CHARS", 5000))

    GATEWAY_URL: str = os.getenv("GATEWAY_URL")
    GATEWAY_API_KEY: str = os.getenv("GATEWAY_API_KEY")


    EMBEDDING_DIMENSIONS = 512

    # Configuración de la BD vectorial
    CHROMA_DIR: str = f"chroma_db_{EMBEDDING_DIMENSIONS}"


# Crear instancia global de settings
settings = Settings()

# Validaciones
#if not settings.GROQ_API_KEY:
#    raise RuntimeError("Falta la variable GROQ_API_KEY en el archivo .env")

if not settings.GATEWAY_API_KEY:
    raise RuntimeError("Falta GATEWAY_API_KEY en el .env")

if not settings.GATEWAY_URL:
    raise RuntimeError("Falta GATEWAY_URL en el .env")