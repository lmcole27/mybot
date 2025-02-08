import chromadb # type: ignore
from chromadb.utils import embedding_functions # type: ignore
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


CHROMA_DATA_PATH = "car_review_embeddings"
EMBED_MODEL = "all-MiniLM-L6-v2"
COLLECTION_NAME = "car_reviews"

client = chromadb.PersistentClient(path=CHROMA_DATA_PATH)

embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBED_MODEL
)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_func,
)

great_reviews = collection.query(
    query_texts=["Find me some positive reviews that discuss the car's performance"],
    n_results=10,
    include=["documents"],
    where ={"Rating":{"$gte":3}}
)
# print("0")
# print(great_reviews["documents"][0])

reviews_str = ",".join(great_reviews["documents"][0])
# print("1")
# print(reviews_str)

#API INFO
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'], organization=os.environ['ORGANIZATION'], project=os.environ['PROJECT'])

question = "What's the key to great customer satisfaction?"
context = "You are a customer success employee at a large car dealership.Use the following car reviews to answer questions: {}"
# print("2")
# print(context.format(reviews_str))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": question}, 
                {"role": "system", "content": context.format(reviews_str)}],
    stream=True)

for chunk in response:
    print(chunk.choices[0].delta.content or "", end="")