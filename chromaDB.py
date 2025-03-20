import chromadb
from chromadb.utils import embedding_functions
#from sentence_transformers import SentenceTransformer

CHROMA_DATA_PATH = "wsib_data/"
EMBED_MODEL = "all-MiniLM-L6-v2"
COLLECTION_NAME = "premium_rates"

client = chromadb.PersistentClient(path=CHROMA_DATA_PATH)

embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBED_MODEL
)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_func,
    metadata={"hnsw:space": "cosine"},)

documents = []

metadata = [{"Data Custodian Email":"data_governance@wsib.on.ca","Data Custodian Branch":"Actuarial Services","Date Range":"January 1, 2016 - December 31, 2020","Date Created":"December 22, 2017","Date Published":"December 11, 2019","Contains Geographic Markers":"No","Update Frequency":"annual","Access Level":"Open/Public","License Type":"Open Government Licence","File Extensions":"csv"},
            {}]


