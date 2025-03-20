import json

print("hello world")
with open ("chat_history.json") as jsonfile:
    conversationHistory = json.load(jsonfile)
print(conversationHistory, "1")

with open('chat_history.json') as user_file:
  file_contents = user_file.read()

print(file_contents)