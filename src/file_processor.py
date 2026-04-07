import os
import pandas as pd
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

# Ruta del archivo CSV

DATA_PATH = "data"

def load_csv(path: str) -> str:
    df = pd.read_csv(path)
    return df.to_string(index=False)

def load_markdown(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def load_image_stub(path: str) -> str:
    """
    Placeholder para OCR.
    Aquí luego puedes integrar Tesseract, Azure Vision, etc.
    """
    return f"[Imagen detectada: {os.path.basename(path)}]"

def chunk_all_files() -> list[Document]:
    documents: list[Document] = []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )

    for filename in os.listdir(DATA_PATH):
        file_path = os.path.join(DATA_PATH, filename)

        if filename.lower().endswith(".csv"):
            text = load_csv(file_path)

        elif filename.lower().endswith((".md", ".markdown")):
            text = load_markdown(file_path)

        elif filename.lower().endswith((".png", ".jpg", ".jpeg")):
            text = load_image_stub(file_path)

        else:
            continue  # ignorar tipos no soportados

        chunks = splitter.split_text(text)

        for chunk in chunks:
            documents.append(
                Document(
                    page_content=chunk,
                    metadata={
                        "source": filename,
                        "type": filename.split(".")[-1]
                    }
                )
            )

    return documents