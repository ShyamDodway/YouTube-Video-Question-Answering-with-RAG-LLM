import streamlit as st
from dotenv import load_dotenv
import os
from utils import fetch_transcript, create_vector_store, build_rag_chain

# Load API key
load_dotenv()

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
            transcript = fetch_transcript(video_id)
        if transcript is None:
            st.error("Transcript not available for this video.")
        else:
            with st.spinner("Creating embeddings and searching..."):
                retriever = create_vector_store(transcript)
                chain = build_rag_chain(retriever)
                answer = chain.invoke(question)
            st.success("✅ Answer:")
            st.write(answer)
