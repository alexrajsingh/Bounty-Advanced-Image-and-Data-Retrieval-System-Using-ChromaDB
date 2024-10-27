# app/embeddings.py

import numpy as np
# Import your model’s module here (e.g., from sentence_transformers or transformers library)
from sentence_transformers import SentenceTransformer  

def get_embedding(text):
    # Initialize model within function to avoid circular import
    model = SentenceTransformer('all-MiniLM-L6-v2')  # Replace with your specific model path if needed
    embedding = model.encode(text)
    return np.array(embedding).flatten()  # Ensure it's a 1D array for ChromaDB compatibility
