from transformers import pipeline

generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_answer(context, question):
    prompt = f"Use the context below to answer the question:\nContext: {context}\n\nQuestion: {question}\nAnswer:"
    result = generator(prompt, max_length=200)
    return result[0]['generated_text']
