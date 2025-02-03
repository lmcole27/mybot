from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()    

OPENAI_API_KEY= os.environ['OPENAI_API_KEY']

#API INFO
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'], 
                organization=os.environ['ORGANIZATION'], 
                project=os.environ['PROJECT'])


stream = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4o",
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")