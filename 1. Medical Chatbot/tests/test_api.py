import pytest
from unittest.mock import patch, MagicMock
from api.main import app
import os

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('api.main.create_rag_chain')
def test_ask_endpoint(mock_create_chain, client):
    # Setup mock
    mock_chain = MagicMock()
    mock_chain.invoke.return_value = {"result": "L'asthme est une maladie respiratoire."}
    mock_create_chain.return_value = mock_chain

    # Mock environment variables
    with patch.dict('os.environ', {'PINECONE_API_KEY': 'fake', 'HUGGINGFACEHUB_API_TOKEN': 'fake'}):
        # We need to make sure the global qa_chain in api.main is reset for each test
        import api.main
        api.main.qa_chain = None

        response = client.post('/ask', json={'question': "Qu'est-ce que l'asthme ?"})

        if response.status_code != 200:
            print(f"Error response: {response.get_json()}")

        assert response.status_code == 200
        data = response.get_json()
        assert 'answer' in data
        assert data['answer'] == "L'asthme est une maladie respiratoire."

def test_ask_no_question(client):
    response = client.post('/ask', json={})
    assert response.status_code == 400
    assert 'error' in response.get_json()

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
