# 🎥 YouTube Q&A Bot with RAG + LangChain

A Retrieval-Augmented Generation (RAG) app that lets users **ask questions about any YouTube video**.  
The app extracts the video transcript, stores it in a vector database (FAISS), and answers user queries with context-aware responses using **LangChain + OpenAI**.  

👉 Live Demo (optional): [Add your Streamlit/Hugging Face link here]

---

## ✨ Features
- 📌 Extracts transcripts from YouTube videos  
- 🔎 Splits transcript into chunks & creates vector embeddings  
- 🤖 Uses **LLM (GPT-3.5/4)** to answer questions based only on video content  
- 🎯 Built with **LangChain, FAISS, OpenAI API, and Streamlit**  
- 📝 Extendable: multi-video RAG, summaries, speaker attribution  

---

## 🛠️ Tech Stack
- [LangChain](https://www.langchain.com/)  
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


### 2. Install Dependencies
pip install -r requirements.txt

### 3. Set OpenAI API Key

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here


Or set it in your terminal:

# Mac/Linux
export OPENAI_API_KEY="your_api_key_here"

# Windows
setx OPENAI_API_KEY "your_api_key_here"

### 4. Run the App
streamlit run app.py

### 📂 Project Structure
youtube-rag-bot/
│── app.py              # Streamlit app
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
│── .env.example        # Example environment variables

