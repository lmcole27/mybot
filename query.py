
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions

# Load Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize ChromaDB client
chroma_client = chromadb.Client()
collection = chroma_client.get_collection(name="insurance_classes")

def chatbot_query(user_query):
    """
    Chatbot function that processes user input and queries ChromaDB.
    """

    # Step 1: Convert user query to embeddings
    query_embedding = model.encode([user_query]).tolist()

    # Step 2: Perform a similarity search in ChromaDB
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3  # Get top 3 most relevant matches
    )

    # Step 3: Format response
    if results and results["ids"]:
        response_text = "Here are the most relevant results:\n"
        for i, metadata in enumerate(results["metadatas"][0]):
            response_text += (
                f"\n🔹 **Class {metadata['Class']}** ({metadata['Class Description']})\n"
                f"   - **Rate:** ${metadata['Class Rate for 2020']}\n"
            )
    else:
        response_text = "Sorry, I couldn't find relevant results. Try rephrasing your query."

    return response_text

# # Example Usage:
# user_input = "Which industries have the highest insurance rates?"
# response = chatbot_query(user_input)
# print(response)
