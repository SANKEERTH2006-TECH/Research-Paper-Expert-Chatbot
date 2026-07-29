"""
====================================================
Research Paper Explanation Generator
====================================================
"""

from transformers import pipeline

print("Loading FLAN-T5 Explainer...")

explainer = pipeline(
    task="text2text-generation",
    model="google/flan-t5-base"
)

print("Explainer Loaded Successfully!")


def explain_concept(question, summary):

    prompt = f"""
You are an AI Research Assistant.

Using the research summary below, answer the user's question in simple language.

Question:
{question}

Research Summary:
{summary}

Explanation:
"""

    result = explainer(
        prompt,
        max_new_tokens=250,
        do_sample=False
    )

    return result[0]["generated_text"].strip()