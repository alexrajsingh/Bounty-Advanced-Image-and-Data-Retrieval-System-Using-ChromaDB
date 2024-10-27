import numpy as np
from sentence_transformers import SentenceTransformer  

def get_embedding(text):
    model = SentenceTransformer('all-MiniLM-L6-v2') 
    embedding = model.encode(text)
    return np.array(embedding).flatten() 
