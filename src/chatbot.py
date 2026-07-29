"""
====================================================
Research Paper Expert Chatbot
Core Chatbot Logic
====================================================
"""

from src.retriever import PaperRetriever
from src.summarizer import summarize_text
from src.explainer import explain_concept
from src.memory import memory


# ---------------------------------------------------
# Initialize Retriever
# ---------------------------------------------------

retriever = PaperRetriever()


# ---------------------------------------------------
# Main Chat Function
# ---------------------------------------------------

def search_and_answer(question):

    # Retrieve relevant papers
    results = retriever.search_with_scores(question, k=3)

    if len(results) == 0:

        return {
            "answer": "No relevant research papers found.",
            "summary": "",
            "papers": [],
            "context": ""
        }

    papers = []

    combined_context = ""

    for doc, score in results:

        metadata = doc.metadata

        title = metadata.get("title", "Unknown Title")

        authors = metadata.get("authors", "Unknown Authors")

        category = metadata.get("categories", "Unknown Category")

        papers.append({

            "title": title,

            "authors": authors,

            "category": category,

            "score": round(float(score), 4)

        })

        combined_context += "\n\n" + doc.page_content

    # Keep prompt manageable
    combined_context = combined_context[:2500]

    # Summarize retrieved content
    summary = summarize_text(combined_context)

    # Include previous conversation for follow-up questions
    previous_context = memory.get_context()

    explanation = explain_concept(

        question=question,

        summary=previous_context + "\n\n" + summary

    )

    memory.add(question, explanation)

    return {

        "answer": explanation,

        "summary": summary,

        "papers": papers,

        "context": combined_context

    }


# ---------------------------------------------------
# Clear Conversation
# ---------------------------------------------------

def clear_history():

    memory.clear()


# ---------------------------------------------------
# Get Conversation History
# ---------------------------------------------------

def get_history():

    return memory.get_history()