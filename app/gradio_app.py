# app/gradio_app.py
import gradio as gr
from app.search import search_documents

def retrieve_documents(query):
    print(f"Query: {query}")
 
    results = search_documents(query)

    # Ensure results["documents"] is a list of dictionaries
    if not isinstance(results["documents"], list):
        return "No documents found."

    # Format each document in the results list
    formatted_results = "\n\n".join(
        [f"Document ID: {results['ids'][0][i]}, Score: {results['distances'][0][i]}\nMetadata: {results['metadatas'][0][i]} Title: {results['metadatas'][0][i].get('title', 'No title available')}\nDocument: {results['documents'][0][i]}"
         for i in range(len(results["documents"][0]))]  # Loop over the inner list
    )

    return formatted_results

# Define Gradio Interface
iface = gr.Interface(
    fn=retrieve_documents,
    inputs="text",
    outputs="text",
    title="Medical Document Retrieval System",
    description="Enter symptoms or keywords to find relevant medical documents.",
    examples=["type 2 diabetes treatment", "hypertension case study", "heart disease symptoms"]
)

if __name__ == "__main__":
    iface.launch()
