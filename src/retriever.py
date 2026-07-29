"""
====================================================
Research Paper Retriever
Loads Existing Chroma Vector Database
====================================================
"""

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


class PaperRetriever:

    def __init__(self):

        print("Loading Vector Database...")

        self.embedding = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.db = Chroma(
            persist_directory="vectordb",
            embedding_function=self.embedding
        )

        print("Vector Database Loaded Successfully!")

    # --------------------------------------------------

    def search(
        self,
        query,
        k=3
    ):

        retriever = self.db.as_retriever(
            search_kwargs={"k": k}
        )

        docs = retriever.invoke(query)

        return docs

    # --------------------------------------------------

    def search_with_scores(
        self,
        query,
        k=3
    ):

        results = self.db.similarity_search_with_score(
            query,
            k=k
        )

        return results