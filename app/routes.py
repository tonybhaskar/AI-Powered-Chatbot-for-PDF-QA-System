


from flask import Blueprint, request, jsonify
from src.llm import get_llm, get_embedding_client, generate_response
from src.database import get_chromadb_collection, populate_chromadb
from src.parser import load_raw_data, parse_documents
from src.utils import handle_exception

# Flask Blueprint
routes = Blueprint('routes', __name__)

# Constants
INPUT_DIR = "data"
CHROMADB_COLLECTION_NAME = "my_collection"

# Initialize Components
llm = get_llm()
embedding_client = get_embedding_client()
collection = get_chromadb_collection(CHROMADB_COLLECTION_NAME)

@routes.route('/load-data', methods=['POST'])
@handle_exception
def load_data_endpoint():
    raw_data = load_raw_data(INPUT_DIR)
    nodes = parse_documents(raw_data)
    embeddings = [embedding_client.get_text_embedding(node.text) for node in nodes]
    populate_chromadb(collection, nodes, embeddings)
    return jsonify({"message": "Data loaded and indexed successfully.", "documents_count": len(nodes)})

@routes.route('/query', methods=['POST'], endpoint='query_data')
@handle_exception
def query_endpoint():
    data = request.json
    query_text = data.get("query", "")
    query_embedding = embedding_client.get_text_embedding(query_text)
    results = collection.query(query_embeddings=[query_embedding], n_results=5)
    response = generate_response(llm, results["documents"], query_text)
    return jsonify({"query": query_text, "response": response, "documents": results["documents"]})
