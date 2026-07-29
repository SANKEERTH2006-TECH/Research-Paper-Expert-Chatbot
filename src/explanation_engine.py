from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)

def explain_concept(concept):
    prompt = f"Explain the concept '{concept}' in simple beginner-friendly language with an example."

    result = generator(
        prompt,
        max_new_tokens=200,
        do_sample=False
    )

    return result[0]["generated_text"]