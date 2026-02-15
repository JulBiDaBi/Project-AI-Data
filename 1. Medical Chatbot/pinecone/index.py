import os
import numpy as np
import re
from pinecone import Pinecone, ServerlessSpec
from utils.preprocessing import upload_to_pinecone

# Define home directory
HOME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run_indexing():
    # Paths
    chunked_output_path = os.path.join(HOME, 'Data', 'processed', 'medical_chunks.txt')
    embedding_path = os.path.join(HOME, 'Data', 'processed', 'medical_chunks_embeddings.npy')

    # Load chunks
    if not os.path.exists(chunked_output_path):
        print(f"Error: {chunked_output_path} not found.")
        return

    with open(chunked_output_path, 'r', encoding='utf-8') as f:
        content = f.read()
    chunks = re.split(r'--- Chunk \d+ ---\n', content)
    chunks = [chunk.strip() for chunk in chunks if chunk.strip()]

    # Load embeddings
    if not os.path.exists(embedding_path):
        print(f"Error: {embedding_path} not found.")
        return
    embeddings = np.load(embedding_path)

    # Pinecone parameters
    PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
    if not PINECONE_API_KEY:
        print("Error: PINECONE_API_KEY environment variable not set.")
        return

    INDEX_NAME = "medical-chatbot-index"

    # Pinecone setup
    pc = Pinecone(api_key=PINECONE_API_KEY)

    # Create index if it doesn't exist
    if INDEX_NAME not in [idx.name for idx in pc.list_indexes()]:
        print(f"Creating index {INDEX_NAME}...")
        pc.create_index(
            name=INDEX_NAME,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )

    index = pc.Index(INDEX_NAME)

    # Upload to Pinecone
    print(f"Uploading {len(embeddings)} vectors to Pinecone...")
    upload_to_pinecone(embeddings, chunks, index)
    print("Indexing complete.")

if __name__ == "__main__":
    run_indexing()
