#https://realpython.com/chromadb-vector-database/

import numpy as np

v1 = np.array([1, 0])
v2 = np.array([0, 1])
v3 = np.array([np.sqrt(2), np.sqrt(2)])

# Dimension
a = v1.shape


# Magnitude - 2 ways to calculate the Euclidean norm
b = np.sqrt(np.sum(v1**2))

c = np.linalg.norm(v1)


d = np.linalg.norm(v3)


# Dot product - 2 ways to calculate the dot product
e = np.sum(v1 * v2)

f = v1 @ v3

# print(a,b,c,d,e,f)
# print(e)
# print(f)

# v1 and v2 are unit vectors because their magnitude, given by the arrow length, is one. v3 isn’t a unit vector, and its magnitude is two, twice the size of v1 and v2.

# v1 and v2 are orthogonal because their tails meet at a 90 degree angle. You see this visually but can also verify it computationally by computing the dot product between v1 and v2. By using the dot product definition, v1 ⋅ v2 = ||v1|| ||v2|| cos(θ), you can see that when θ = 90, cos(θ) = 0 and v1 ⋅ v2 = 0. Intuitively, you can think of v1 and v2 as being totally unrelated or having nothing to do with each other. This will become important later.

# v3 makes a 45 degree angle with both v1 and v2. This means that v3 will have a non-zero dot product with v1 and v2. This also means that v3 is equally related to both v1 and v2. In general, the smaller the angle between two vectors, the more they point toward a common direction.

import spacy

nlp = spacy.load("en_core_web_md")

dog_embedding = nlp.vocab["dog"].vector

print(type(dog_embedding))
print(dog_embedding.shape)
print(dog_embedding[:10])
