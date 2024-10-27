from chromadb import Client
from chromadb.config import Settings
from app.embeddings import get_embedding
from app.chromadb_setup import collection

client = Client(Settings()) 
collection = client.get_or_create_collection("medical_documents")

def search_documents(query):
    embedding = get_embedding(query)
    print(f"Embedding shape: {embedding.shape}")
    
    results = collection.query(
        query_embeddings=[embedding.tolist()], 
        n_results=1  
    )
    
    return results

