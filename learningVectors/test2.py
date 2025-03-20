import chromadb
from chromadb.utils import embedding_functions

DATA_PATH = "data/archive/*"
CHROMA_PATH = "car_review_embeddings"
EMBEDDING_FUNC_NAME = "multi-qa-MiniLM-L6-cos-v1"
COLLECTION_NAME = "car_reviews"

client = chromadb.PersistentClient(CHROMA_PATH)
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
         model_name=EMBEDDING_FUNC_NAME
     )
collection = client.get_collection(name=COLLECTION_NAME, embedding_function=embedding_func)

great_reviews = collection.query(
    query_texts=["Find me some positive reviews that discuss the car's performance"],
    n_results=5,
    include=["documents", "distances", "metadatas"]
)

print(great_reviews["documents"][0][0])
#' Great all around car with great balance of performance and comfort. Terrific technology too.'