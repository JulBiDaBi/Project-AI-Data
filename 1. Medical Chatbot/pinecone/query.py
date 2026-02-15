import os
from utils.preprocessing import create_rag_chain

def run_query(question):
    # Pinecone parameters
    PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
    HUGGINGFACEHUB_API_TOKEN = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
    INDEX_NAME = "medical-chatbot-index"

    if not PINECONE_API_KEY or not HUGGINGFACEHUB_API_TOKEN:
        print("Error: PINECONE_API_KEY or HUGGINGFACEHUB_API_TOKEN not set.")
        return

    # Create RAG chain
    qa_chain = create_rag_chain(
        index_name=INDEX_NAME,
        pinecone_api_key=PINECONE_API_KEY,
        embeddings_model_name="sentence-transformers/all-MiniLM-L6-v2",
        huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN
    )

    # Run query
    print(f"Question: {question}")
    result = qa_chain.invoke(question)
    print(f"Answer: {result['result']}")

if __name__ == "__main__":
    sample_question = "Qu'est-ce que l'asthme ?"
    run_query(sample_question)
