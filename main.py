#import chromadb
#import pandas as pd
#from io import StringIO
#from sentence_transformers import SentenceTransformer
#from cosine_similarity import compute_cosine_similarity
#from query import chatbot_query 

from openai import OpenAI
from flask import Flask, render_template, request, Response, stream_with_context, jsonify
import json
import os
from dotenv import load_dotenv
from history import load_chat, add_message, save_chat

load_dotenv()


# # Load Sentence Transformer model
# model = SentenceTransformer("all-MiniLM-L6-v2")

# # Initialize ChromaDB client
# chroma_client = chromadb.Client()
# collection = chroma_client.get_collection(name="insurance_classes")

#API INFO
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'], organization=os.environ['ORGANIZATION'], project=os.environ['PROJECT'])
chat_history = load_chat()

#CREATE WEBAPP
app = Flask(__name__)

def generate_response(question: str):
    # Send API request to ChatGPT and recieve resonse
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}, 
                  {"role": "system", "content": f"consider the conversation context {chat_history}"},
                  {"role": "system", "content":"provide response with HTML tags but no header."
                   }],
        stream=True,
    )

    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            ans = chunk.choices[0].delta.content
            #print(ans, end="")
            yield ans

    
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    question = request.form.get('question')
    if not question:
        return "Please provide a question", 400
    
    # Save question to chat_history
    add_message(chat_history, "user", question)
    save_chat(chat_history)

    def generate():
        for chunk in generate_response(question):
            yield chunk

    return Response(stream_with_context(generate()), mimetype='text/plain')


# Example Usage:
# user_input = "Which industries have the highest insurance rates?"
# response = chatbot_query(user_input)
# print(response)

@app.route('/api/endpoint', methods=['POST'])
def receive_post():
    try:
        # Get JSON data from the request
        data = request.get_json()
        response = data["message"]
        # Save response to chat_history
        add_message(chat_history, "assistant", response)
        save_chat(chat_history)

        # Respond back to client
        return jsonify({"message": "Data received successfully", "received": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


#RUN THE WEBAPP
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)


    