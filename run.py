# run.py

from app.chromadb_setup import load_data
from app.gradio_app import iface

# Load data into ChromaDB (run once)
load_data()

# Launch Gradio interface
iface.launch()
