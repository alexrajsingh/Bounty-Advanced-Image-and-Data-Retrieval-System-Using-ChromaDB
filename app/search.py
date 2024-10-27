# app/search.py

from chromadb import Client
from chromadb.config import Settings
from app.embeddings import get_embedding
from app.chromadb_setup import collection

# Initialize ChromaDB Client without the `database` parameter
client = Client(Settings())  # Using default settings
collection = client.get_or_create_collection("medical_documents")

def search_documents(query):
    # Get the embedding for the query
    embedding = get_embedding(query)
    print(f"Embedding shape: {embedding.shape}")
    
    # Use 'query_embeddings' as the parameter name and provide it in the correct format
    results = collection.query(
        query_embeddings=[embedding.tolist()],  # Ensure this is a list of lists
        n_results=1  # Retrieve the top result(s); adjust as needed
    )
    
    return results

