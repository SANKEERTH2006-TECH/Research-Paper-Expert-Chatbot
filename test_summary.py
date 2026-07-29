from src.retriever import PaperRetriever
from src.summarizer import summarize_text

retriever = PaperRetriever()

docs = retriever.search(
    "What is Reinforcement Learning?"
)

text = docs[0].page_content

summary = summarize_text(text)

print("=" * 60)

print(summary)