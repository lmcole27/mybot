from openai import OpenAI
from flask import Flask, render_template, request, Response, stream_with_context
import chromadb
import pandas as pd
from io import StringIO
from sentence_transformers import SentenceTransformer
from cosine_similarity import compute_cosine_similarity
from query import chatbot_query 

import os
from dotenv import load_dotenv

load_dotenv()


# # Load Sentence Transformer model
# model = SentenceTransformer("all-MiniLM-L6-v2")

# # Initialize ChromaDB client
# chroma_client = chromadb.Client()
# collection = chroma_client.get_collection(name="insurance_classes")

#API INFO
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'], organization=os.environ['ORGANIZATION'], project=os.environ['PROJECT'])


#CREATE WEBAPP
app = Flask(__name__)

def generate_response(question: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}, 
                  {"role": "system", #"content":"cite references",
                   "content":"provide response with HTML tags but no header."
                   }],
        stream=True,
    )

    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            ans = chunk.choices[0].delta.content
            print(ans, end="")
            yield ans

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    question = request.form.get('question')
    if not question:
        return "Please provide a question", 400

    def generate():
        for chunk in generate_response(question):
            yield chunk

    return Response(stream_with_context(generate()), mimetype='text/plain')


# Example Usage:
user_input = "Which industries have the highest insurance rates?"
response = chatbot_query(user_input)
print(response)

#RUN THE WEBAPP
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


    