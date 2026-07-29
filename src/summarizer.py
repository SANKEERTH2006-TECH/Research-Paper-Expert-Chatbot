"""
====================================================
Research Paper Summarizer
====================================================
"""

from transformers import pipeline

print("Loading FLAN-T5 Summarizer...")

summarizer = pipeline(
    task="text2text-generation",
    model="google/flan-t5-base"
)

print("Summarizer Loaded Successfully!")


def summarize_text(text):

    if len(text) > 1800:
        text = text[:1800]

    prompt = f"""
Summarize the following research paper in simple language.

{text}

Summary:
"""

    result = summarizer(
        prompt,
        max_new_tokens=180,
        do_sample=False
    )

    return result[0]["generated_text"].strip()