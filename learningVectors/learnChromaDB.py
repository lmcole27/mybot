import chromadb # type: ignore
from chromadb.utils import embedding_functions # type: ignore

CHROMA_DATA_PATH = "chroma_data/"
EMBED_MODEL = "all-MiniLM-L6-v2"
COLLECTION_NAME = "demo_docs"

client = chromadb.PersistentClient(path=CHROMA_DATA_PATH)

embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBED_MODEL
)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_func,
    metadata={"hnsw:space": "cosine"},
)

documents = [
    "Artificial intelligence is transforming the technology landscape.",
    "Traveling to new places can broaden one's perspective.",
    "The study of quantum physics is fascinating and complex.",
    "Delicious food can bring people together.",
    "The Renaissance was a pivotal period in art history.",
    "Regular exercise is essential for maintaining good health.",
    "The Mona Lisa is one of the most famous paintings in art history.",
    "Climate change poses a significant threat to the planet's ecosystems and biodiversity.",
    "Startup companies often face challenges in securing funding and scaling their operations.",
    "Beethoven's Symphony No. 9 is celebrated for its powerful choral finale, 'Ode to Joy.'",
    ]

genres = [
    "technology",
    "travel",
    "science",
    "food",
    "history",
    "fitness",
    "art",
    "climate change",
    "business",
    "music",
]

collection.add(
    documents=documents,
    ids=[f"id{i}" for i in range(len(documents))],
    metadatas=[{"genre": g} for g in genres]
)

query_results = collection.query(
    query_texts=["Find me some delicious food!"],
    n_results=1,
)

print(query_results.keys())
#dict_keys(['ids', 'distances', 'metadatas', 'embeddings', 'documents'])

print(query_results["documents"])
#[['Traditional Italian pizza is famous for its thin crust, fresh ingredients, and wood-fired ovens.']]

print(query_results["ids"])
#[['id3']]

print(query_results["distances"])
#[[0.7638263782124082]]

print(query_results["metadatas"])
#[[{'genre': 'food'}]]