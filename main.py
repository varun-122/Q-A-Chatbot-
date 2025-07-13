from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import wikipedia
from transformers import pipeline

app = FastAPI()

# Static folder mount for CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Load model once
generator = pipeline("text2text-generation", model="google/flan-t5-base")

def fetch_wikipedia_summary(query):
    try:
        summary = wikipedia.summary(query, sentences=5)
        return summary
    except wikipedia.exceptions.PageError:
        return "No article found for this query."
    except wikipedia.exceptions.DisambiguationError:
        return "Query is ambiguous, please be more specific."

def generate_answer(context, question):
    prompt = f"Use the context below to answer the question:\nContext: {context}\n\nQuestion: {question}\nAnswer:"
    result = generator(prompt, max_length=200)
    return result[0]['generated_text']

@app.get("/", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@app.post("/chat/", response_class=HTMLResponse)
def chat(request: Request, question: str = Form(...)):
    query = question.strip().capitalize()
    context = fetch_wikipedia_summary(query)
    answer = generate_answer(context, question)
    return templates.TemplateResponse("chat.html", {
        "request": request,
        "question": question,
        "context": context,
        "answer": answer
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
