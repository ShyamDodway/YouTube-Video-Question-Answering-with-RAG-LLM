# 🎬 YouTube Transcript Q&A (LangChain + Streamlit)

An interactive app that lets you **ask questions about any YouTube video** using its transcript — powered by **LangChain**, **OpenAI**, and **FAISS**.

## 🚀 Features
- Fetches transcripts automatically using `youtube-transcript-api`
- Builds embeddings using OpenAI’s `text-embedding-3-small`
- Uses a vector retriever + GPT model to answer from transcript context
- Simple Streamlit interface

## 🧩 Setup Instructions

1. Clone the repo  
   ```bash
   git clone https://github.com/yourusername/youtube-rag-app.git
   cd youtube-rag-app
