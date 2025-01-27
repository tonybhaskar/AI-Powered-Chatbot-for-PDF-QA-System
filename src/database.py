import chromadb

# Initialize ChromaDB
def get_chromadb_collection(collection_name):
    client = chromadb.Client()
    return client.get_or_create_collection(collection_name)

# Populate ChromaDB
def populate_chromadb(collection, nodes, embeddings):
    for idx, embedding in enumerate(embeddings):
        collection.add(
            documents=[nodes[idx].text],
            embeddings=[embedding],
            metadatas=[{"id": f"doc_{idx}"}],
            ids=[f"doc_{idx}"]
        )
