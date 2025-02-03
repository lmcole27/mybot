from flask import Flask, render_template, request, stream_template
from openai import OpenAI

import os
from dotenv import load_dotenv

load_dotenv()

#CREATE WEBAPP
app = Flask(__name__)

#API INFO
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'], 
                organization=os.environ['ORGANIZATION'], 
                project=os.environ['PROJECT'])


#WEB HOME PAGE
@app.route('/', methods=['GET', 'POST'])
def welcome():
    if request.method== 'POST':
        prompt= request.form.get('question')
        print(f"This is the quetion: {prompt}")
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            stream=True,
            )
        print("Hi, How are you?")
        for chunk in stream:
            print(chunk)
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content or "", end="")
                text = chunk.choices[0].delta.content
                print(text)
                if len(text): 
                    print(text)
                    yield text
        return stream_template('index.html')
    else:
        return render_template("index.html")
    

#RUN THE WEBAPP
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
