import chromadb
from chromadb.utils import embedding_functions
from car_data_etl import prepare_car_reviews_data
from chroma_utils import build_chroma_collection

DATA_PATH = "data/archive/*"
CHROMA_PATH = "car_review_embeddings"
EMBEDDING_FUNC_NAME = "multi-qa-MiniLM-L6-cos-v1"
COLLECTION_NAME = "car_reviews"

chroma_car_reviews_dict = prepare_car_reviews_data(DATA_PATH)

build_chroma_collection(
     CHROMA_PATH,
     COLLECTION_NAME,
     EMBEDDING_FUNC_NAME,
     chroma_car_reviews_dict["ids"],
     chroma_car_reviews_dict["documents"],
     chroma_car_reviews_dict["metadatas"]
 )