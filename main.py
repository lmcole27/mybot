from openai import OpenAI
from flask import Flask, render_template, request, Response, stream_with_context

import os
from dotenv import load_dotenv

load_dotenv()

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


#THIS WORKED-ISH
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == "POST":
#         question = request.form.get('question')
#         print(f"This is the quetion: {question}")
#         if not question:
#             return "Please provide a question", 400

#         #answer = generate_response(question)
#         def generate():
#             for chunk in generate_response(question):
#                 yield chunk
#         return Response(stream_with_context(generate()), mimetype='text/plain')
#         #return render_template('index.html', answer=generate_response(question))
#     return render_template('index.html')

            # def generate(question):
            #     for chunk in generate_response(question, content=body):
            #         yield chunk
            #     yield "first part"
            #     yield "second part"

            # return render_template('index.html', answer=Response(stream_with_context(generate(question))))        
    # else:
    #     return render_template("index.html", answer="Please submit a question.")
#    return render_template('index.html')


    #return Response(stream_with_context(generate_response(), content_type='text/event-stream'))

# Stream response from OpenAI API
# @app.route('/stream', methods=['GET', 'POST'])

            
#WEB HOME PAGE
# @app.route('/', methods=['GET', 'POST'])
# def welcome():
    # def generate_response():
    #     response = client.chat.completions.create(
    #                     model="gpt-4o-mini",
    #                     messages=[{"role": "user", "content": question}],
    #                     stream=True,
    #                 )
#         for chunk in response:
#             if chunk.choices[0].delta.content is not None:
#                 print(chunk.choices[0].delta.content, end="")
    
#     if request.method == "POST":
#         question = request.form.get('question')
#         print(f"This is the quetion: {question}")

#             # flash("Hmmm... there is a problem with your question. Please try again.") 
#             # return redirect(url_for('/'))   
#         return Response(generate_response(), content_type='text/event-stream')        
#     else:
#         return render_template("index.html")

#RUN THE WEBAPP

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


    