import spacy # type: ignore
from cosine_similarity import compute_cosine_similarity

nlp = spacy.load("en_core_web_md")

dog_embedding = nlp.vocab["dog"].vector
cat_embedding = nlp.vocab["cat"].vector
apple_embedding = nlp.vocab["apple"].vector
tasty_embedding = nlp.vocab["tasty"].vector
delicious_embedding = nlp.vocab["delicious"].vector
truck_embedding = nlp.vocab["truck"].vector
son_embedding = nlp.vocab["son"].vector
boy_embedding = nlp.vocab["boy"].vector
male_embedding = nlp.vocab["male"].vector

print(compute_cosine_similarity(dog_embedding, cat_embedding))  # 0.8220817
print(compute_cosine_similarity(delicious_embedding, tasty_embedding))  # 0.8482092
print(compute_cosine_similarity(apple_embedding, delicious_embedding))  # 0.5347655
print(compute_cosine_similarity(dog_embedding, apple_embedding))  # 0.22881003
print(compute_cosine_similarity(truck_embedding, delicious_embedding))  # 0.08978759
print(compute_cosine_similarity(son_embedding, boy_embedding))  # 0.849
print(compute_cosine_similarity(male_embedding, boy_embedding))