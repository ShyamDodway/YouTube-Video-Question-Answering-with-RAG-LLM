import os
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import YoutubeLoader

def fetch_transcript(video_id: str):
    try:
        url = f"https://www.youtube.com/watch?v={video_id}"

        loader = YoutubeLoader.from_youtube_url(
            url,
            add_video_info=False,
            language=["en"]
        )

        docs = loader.load()

        transcript = " ".join(doc.page_content for doc in docs)

        return transcript

    except Exception as e:
        print(e)
        return None


def create_vector_store(transcript: str):
    """Split transcript and create FAISS vector store."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.create_documents([transcript])
    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

def build_rag_chain(retriever):
    """Create the LangChain pipeline."""
    llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0.2
)
    prompt = PromptTemplate(
        template="""
        You are a helpful assistant.
        Answer ONLY from the provided transcript context.
        If the context is insufficient, say you don't know.

        {context}
        Question: {question}
        """,
        input_variables=['context', 'question']
    )

    def format_docs(retrieved_docs):
        return "\n\n".join(doc.page_content for doc in retrieved_docs)

    parallel_chain = RunnableParallel({
        "context": retriever | RunnableLambda(format_docs),
        "question": RunnablePassthrough()
    })

    parser = StrOutputParser()
    main_chain = parallel_chain | prompt | llm | parser
    return main_chain
