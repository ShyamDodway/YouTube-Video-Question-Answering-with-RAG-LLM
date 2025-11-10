# ==============================
# ✅ Environment Setup for OpenAI Key
# ==============================
import os
import streamlit as st
from dotenv import load_dotenv
import re  # For YouTube link normalization

# Load local .env when running locally
load_dotenv()

# Use key from .env (local) or Streamlit Secrets (cloud)
if "OPENAI_API_KEY" not in os.environ:
    if "OPENAI_API_KEY" in st.secrets:
        os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
    else:
        st.error("⚠️ OpenAI API key not found. Please add it in .env or Streamlit Secrets.")

# ==============================
# 🧠 Utility Function to Normalize YouTube URLs
# ==============================
def normalize_youtube_url(url: str):
    """
    Converts short or long YouTube URLs into a standard format.
    Extracts the 11-character video ID and returns a clean link.
    """
    match = re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})", url)
    if match:
        return match.group(1)
    return None

# ==============================
# 🧠 Main App
# ==============================
from utils import fetch_transcript, create_vector_store, build_rag_chain

st.set_page_config(page_title="YouTube Video Q&A", layout="wide")
st.title("🎬 YouTube Transcript Q&A App")
st.write("Ask questions about any YouTube video using its transcript!")

# ==============================
# 🎯 Sidebar (For HR / Visitors)
# ==============================
with st.sidebar:
    st.header("💡 Quick Demo Example")
    st.write("Try these sample inputs to see how the app works!")

    st.markdown("**Example YouTube Link:**")
    st.code("https://www.youtube.com/watch?v=OcISVEh1jyw", language=None)

    st.markdown("**Example Question:**")
    st.code("Summarize the video", language=None)

    st.markdown("---")
    st.write("🧭 **How to Use:**")
    st.markdown("""
    1. Paste any YouTube video link.  
    2. Type your question about the video.  
    3. Click **Get Answer** to generate a response.  
    """)

# ==============================
# 🔍 Input Fields
# ==============================
video_url = st.text_input("🔗 Enter YouTube Video URL:")
question = st.text_input("❓ Ask your question:")
run_button = st.button("Get Answer")

if run_button:
    video_id = normalize_youtube_url(video_url)

    if not video_url or not video_id:
        st.warning("Please enter a valid YouTube URL.")
    else:
        with st.spinner("Fetching transcript..."):
            try:
                transcript = fetch_transcript(video_id)
            except Exception:
                st.error("❌ Unable to fetch transcript. This video may be private, restricted, or lacks captions.\n Please try another video or one with English transcript.")
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
