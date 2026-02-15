import streamlit as st
import requests
import os

# Configuration
API_URL = os.environ.get("API_URL", "http://localhost:5000/ask")

st.set_page_config(page_title="Medical ChatBot", page_icon="🏥")

st.title("🏥 Medical ChatBot")
st.markdown("Posez vos questions sur la santé basées sur notre base de connaissances médicale.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Votre question ici..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call API
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")

        try:
            response = requests.post(API_URL, json={"question": prompt})
            if response.status_code == 200:
                answer = response.json().get("answer", "No answer received.")
                message_placeholder.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            else:
                error_msg = response.json().get("error", "Error connecting to API")
                message_placeholder.markdown(f"❌ Erreur: {error_msg}")
        except Exception as e:
            message_placeholder.markdown(f"❌ Erreur de connexion : {str(e)}")

st.sidebar.markdown("---")
st.sidebar.info("Ce chatbot utilise une architecture RAG avec Pinecone et LangChain.")
