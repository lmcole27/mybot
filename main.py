from openai import OpenAI
from flask import Flask, render_template, request
#redirect, flash, url_for, Response
#from flask import Flask, render_template, url_for, request, redirect, flash
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField, TelField
# from wtforms.validators import DataRequired
#import requests
import os
from dotenv import load_dotenv

load_dotenv()

#CREATE WEBAPP
app = Flask(__name__)

#API INFO
OPENAI_API_KEY= os.environ['OPENAI_API_KEY']

client = OpenAI(api_key=OPENAI_API_KEY, organization="org-rAHDoRUNzBdwWGvZDAzPtjtA", project="proj_zSIh53fD20WgKUt814U9pIgA")



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        question = request.form.get('question')
        if not question:
            # flash("Hmmm... there is a problem with your question. Please try again.") 
            # return redirect(url_for('/')) 
            return render_template('index.html', answer="Please submit a question.")
        else:
            print(f"This is the quetion: {question}")
            answer = generate_response(question)

            return render_template('index.html', answer=answer)        
    else:
        return render_template("index.html", answer="Please submit a question.")
#    return render_template('index.html')


def generate_response(question):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}, 
                  {"role": "system", "content":"cite references"}],
    #    stream=True,
    
    )
    answer = response.choices[0].message.content
    return answer
    # for chunk in response:
    #     if chunk.choices[0].delta.content is not None:
    #         print(chunk.choices[0].delta.content, end="")
# return Response(generate_response(), content_type='text/event-stream')

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
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


    