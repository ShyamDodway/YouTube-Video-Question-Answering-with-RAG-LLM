#  YouTube RAG App — AI-Powered Video Q&A System

This Streamlit web app uses **LangChain**, **Groq LLM**, **Hugging Face embeddings**, and **YouTube transcripts** to answer user questions and generate contextual responses from any YouTube video.

---

##  Features

*  Extracts transcripts automatically from YouTube videos
*  Uses **Retrieval-Augmented Generation (RAG)** for context-aware question answering
*  Semantic search powered by **FAISS vector database**
*  Fast inference using **Groq LLMs**
*  Free embeddings using **Hugging Face Sentence Transformers**
*  Interactive web interface built with **Streamlit**

---

##  Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **Groq API**
* **Hugging Face Embeddings**
* **FAISS**
* **YouTube Transcript API**

---

##  Project Structure

youtube-rag-app/
│

├── app.py                  # Main Streamlit application

├── utils.py                # Transcript fetching, embeddings, RAG pipeline

├── requirements.txt        # Project dependencies

├── .env                    # Stores Groq API Key (ignored in Git)

├── .gitignore              # Prevents sensitive files from being pushed

└── README.md               # Project documentation

---

##  How It Works

1. User enters a YouTube video URL
2. App fetches the transcript using YouTube Transcript API
3. Transcript is split into chunks and converted into embeddings
4. FAISS performs semantic similarity search
5. Groq LLM generates contextual answers based on retrieved transcript chunks

---

##  Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Create a `.env` file and add:

```env
GROQ_API_KEY=your_api_key_here
```
