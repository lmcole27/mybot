from openai import OpenAI
from flask import Flask, render_template, request
#, Response, stream_with_context
#from typing import Generator
import os
from dotenv import load_dotenv
import logging

#logger = logging.getLogger(__name__)


load_dotenv()


#CREATE WEBAPP
app = Flask(__name__)

#API INFO
#API INFO
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'], 
                organization=os.environ['ORGANIZATION'], 
                project=os.environ['PROJECT'])

@app.route('/', methods=['GET', 'POST'])
def stream_openai_response():
    if request.method == "POST":
        prompt = request.form.get('question')
        if not prompt:
            logging. Error("Received empty prompt")
            yield "data: Error: Received empty prompt\n\n"
            return render_template("index.html")
   
    # Proceed with existing code to call OpenAI API
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        #temperature=0.5,
        messages=[{"role": "user", "content": prompt},
                  {"role": "system", "content":"cite references"}],
        stream=True,
    )

    for event in stream:
        # Log the event to console
        logging.info(f"Streaming event: {event}")
        try:
            # Extract the content from the event
            if 'choices' in event and len(event['choices']) > 0:
                text = event['choices'][0].get('message', {}).get('content', '')
                if text:  # Ensure there is text to send
                    formatted_data = f"data: {text}\n\n"
                    logging.info(f"Formatted for SSE: {formatted_data}")
                    yield formatted_data
                else:
                    logging.info("No text to send, skipping.")
            else:
                logging. Warning(f"Unexpected event format: {event}")
        except Exception as e:
            logging. Error(f"Error while processing stream: {e}")
            yield f"data: Error: {str(e)}\n\n"

    return render_template("index.html")

#RUN THE WEBAPP
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)