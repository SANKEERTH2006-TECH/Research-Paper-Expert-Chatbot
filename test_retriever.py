from src.retriever import PaperRetriever

retriever = PaperRetriever()

query = "Explain Reinforcement Learning"

results = retriever.search(query)

print("=" * 60)

for i, doc in enumerate(results, 1):

    print(f"\nPaper {i}")

    print("-" * 40)

    print(doc.page_content[:800])