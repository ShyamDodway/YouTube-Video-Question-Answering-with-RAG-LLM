🎥 YouTube Q&A Bot with RAG + LangChain

A Retrieval-Augmented Generation (RAG) app that lets users ask questions about any YouTube video.
The app extracts the video transcript, stores it in a vector database (FAISS), and answers user queries with context-aware responses using LangChain + OpenAI.

👉 Live Demo (optional): [Add your Streamlit/Hugging Face link here]

✨ Features

📌 Extracts transcripts from YouTube videos

🔎 Splits transcript into chunks & creates vector embeddings

🤖 Uses LLM (GPT-3.5/4) to answer questions based only on video content

🎯 Built with LangChain, FAISS, OpenAI API, and Streamlit

📝 Extendable: multi-video RAG, summaries, speaker attribution

🛠️ Tech Stack

LangChain

OpenAI API

FAISS

Streamlit

YouTube Transcript API

⚡ Setup Instructions
1. Clone the Repo
git clone https://github.com/your-username/youtube-rag-bot.git
cd youtube-rag-bot

2. Install Dependencies
pip install -r requirements.txt

3. Set OpenAI API Key

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here


Or set it in your terminal:

export OPENAI_API_KEY="your_api_key_here"  # Mac/Linux
setx OPENAI_API_KEY "your_api_key_here"   # Windows

4. Run the App
streamlit run app.py

📂 Project Structure
youtube-rag-bot/
│── app.py              # Streamlit app
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
│── .env.example        # Example environment variables

🚀 Future Improvements

Multi-video RAG → Ask across multiple videos

Summarization mode → Generate bullet-point summaries

Speaker attribution (if transcript supports)

Deployment to Hugging Face / Streamlit Cloud

🧑‍💻 Author

👤 Your Name

GitHub: @your-username

LinkedIn: Your LinkedIn
