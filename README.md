# 🎥 YouTube Q&A with RAG + LLM

A Retrieval-Augmented Generation (RAG) app that lets users **ask questions about any YouTube video**.  
The app extracts the video transcript, stores it in a vector database (FAISS), and answers user queries with context-aware responses using **OpenAI**.  

👉 Live Demo (optional): [Add your Streamlit/Hugging Face link here]

---

## ✨ Features
- 📌 Extracts transcripts from YouTube videos  
- 🔎 Splits transcript into chunks & creates vector embeddings  
- 🤖 Uses **LLM (GPT-3.5/4)** to answer questions based only on video content  
- 🎯 Built with **FAISS, OpenAI API, and Streamlit**  
- 📝 Extendable: multi-video RAG, summaries, speaker attribution  

---

## 🛠️ Tech Stack
- [OpenAI API](https://platform.openai.com/)  
- [FAISS](https://faiss.ai/)  
- [Streamlit](https://streamlit.io/)  
- [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/)  

---

## ⚡ Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/youtube-rag-bot.git
cd youtube-rag-bot

