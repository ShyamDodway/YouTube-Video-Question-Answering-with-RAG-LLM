# ==============================
# ✅ Environment Setup for OpenAI Key
# ==============================
import os
import streamlit as st
from dotenv import load_dotenv

# Load local .env when running locally
load_dotenv()

# Use key from .env (local) or Streamlit Secrets (cloud)
if "OPENAI_API_KEY" not in os.environ:
    if "OPENAI_API_KEY" in st.secrets:
        os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
    else:
        st.error("⚠️ OpenAI API key not found. Please add it in .env or Streamlit Secrets.")

# ==============================
# 🧠 Main App
# ==============================
from utils import fetch_transcript, create_vector_store, build_rag_chain

st.set_page_config(page_title="YouTube Video Q&A", layout="centered")
st.title("🎬 YouTube Transcript Q&A App")
st.write("Ask questions about any YouTube video using its transcript!")

video_url = st.text_input("🔗 Enter YouTube Video URL:")
question = st.text_input("❓ Ask your question:")
run_button = st.button("Get Answer")

if run_button:
    if not video_url or "youtube.com" not in video_url:
        st.warning("Please enter a valid YouTube URL.")
    else:
        video_id = video_url.split("v=")[-1]
        with st.spinner("Fetching transcript..."):
            try:
                transcript = fetch_transcript(video_id)
            except Exception:
                st.error("❌ Unable to fetch transcript. This video may be private, restricted, or lacks captions.\n Please try another video or with english transcript")
                st.stop()

        if not transcript:
            st.warning("⚠️ No transcript found for this video.")
        else:
            with st.spinner("Creating embeddings and searching..."):
                retriever = create_vector_store(transcript)
                chain = build_rag_chain(retriever)
                answer = chain.invoke(question)
            st.success("✅ Answer:")
            st.write(answer)
