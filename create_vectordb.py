from langchain_core.documents import Document

from src.loader import load_arxiv_data
from src.chunker import split_documents
from src.vector_store import create_vector_store

print("=" * 60)
print("Loading Dataset...")

df = load_arxiv_data()

print("Papers Loaded:", len(df))

documents = []

for _, row in df.iterrows():

    documents.append(
        Document(
            page_content=row["summary"],
            metadata={
                "title": row["title"]
            }
        )
    )

print("Splitting Documents...")

chunks = split_documents(documents)

print("Chunks:", len(chunks))

print("Creating Vector Database...")

create_vector_store(chunks)

print("=" * 60)
print("Vector Database Created Successfully!")