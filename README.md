# 🎙️ Q&A Chatbot

An interactive chatbot built with **FastAPI** and **Hugging Face Transformers**. It fetches real-time information from **Wikipedia** and generates responses using local language models, creating a smooth, fully offline Q&A experience.

---

## ✨ Technologies

- **FastAPI** – high-performance web framework for building APIs  
- **Uvicorn** – lightning-fast ASGI server to run FastAPI  
- **Jinja2** – template engine for rendering dynamic HTML pages  
- **Python Libraries**:  
  - `transformers` – pre-trained language models from Hugging Face  
  - `wikipedia` – fetches dynamic content from Wikipedia  
  - `requests` – useful for API calls (usually comes with Python)

---

## 🚀 Features

- 🔍 Real-time Wikipedia content fetching  
- 🤖 NLP-powered chatbot responses using transformers  
- 🌐 FastAPI backend with templated HTML frontend  
- 💻 Fully local deployment — *no paid APIs like OpenAI used*

---

## 📍 The Process

I set out to build a chatbot that could answer user queries dynamically using open-source tools and models.  
- **FastAPI** was chosen for its simplicity and speed in building backend APIs.  
- **Jinja2** helped render clean and responsive HTML pages.  
- I integrated **Hugging Face transformers** to power the chatbot's intelligence and conversation flow.  
- To make it more informative, I used the **wikipedia** Python library to fetch real-time information based on the user's query.  
- The biggest challenge was running large NLP models locally without a GPU — which results in slower response times, but everything remains free and offline.

---

## 🎥 Preview
[▶️ Watch Demo Video](./assets/preview.mp4)
