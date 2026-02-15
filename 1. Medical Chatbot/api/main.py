import os
from flask import Flask, request, jsonify
from utils.preprocessing import create_rag_chain

app = Flask(__name__)

# Global variable for the RAG chain
qa_chain = None

def get_qa_chain():
    global qa_chain
    if qa_chain is None:
        pinecone_api_key = os.environ.get("PINECONE_API_KEY")
        huggingfacehub_api_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
        index_name = "medical-chatbot-index"

        if not pinecone_api_key or not huggingfacehub_api_token:
            return None

        qa_chain = create_rag_chain(
            index_name=index_name,
            pinecone_api_key=pinecone_api_key,
            embeddings_model_name="sentence-transformers/all-MiniLM-L6-v2",
            huggingfacehub_api_token=huggingfacehub_api_token
        )
    return qa_chain

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    if not data or 'question' not in data:
        return jsonify({"error": "No question provided"}), 400

    question = data['question']
    chain = get_qa_chain()
    if chain is None:
        return jsonify({"error": "RAG chain not initialized. Check API keys."}), 500

    try:
        result = chain.invoke(question)
        return jsonify({"answer": result.get('result', 'No answer found.')})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
