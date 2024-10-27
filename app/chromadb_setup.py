import sys
__import__('pysqlite3')
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
from chromadb import Client
from chromadb.config import Settings
import json
import os
from app.embeddings import get_embedding

client = Client(Settings())
collection = client.get_or_create_collection("medical_documents")

def load_data():
    data_path = os.path.join(os.path.dirname(__file__), '../data/medical_data.json')
    
    with open(data_path, 'r') as file:
        documents = json.load(file)
    
    ids = []
    texts = []
    embeddings = []
    metadatas = [] 
    
    for doc in documents:
        ids.append(doc["id"])
        texts.append(doc["text"])
        embeddings.append(get_embedding(doc["text"]))
        metadatas.append({"title": doc.get("title", "Untitled")})  
    
    collection.add(ids=ids, documents=texts, embeddings=embeddings, metadatas=metadatas)
    print("Data loaded into ChromaDB.")

if __name__ == "__main__":
    load_data()
