from app.chromadb_setup import load_data
from app.gradio_app import iface

load_data()

iface.launch()
