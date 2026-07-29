from langchain_chroma import Chroma
from src.embeddings import embedding_model

DB_PATH = "vectordb"

def create_vector_store(documents):
    db = Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        persist_directory=DB_PATH,
    )
    return db

def load_vector_store():
    return Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding_model,
    )