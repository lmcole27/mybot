import json
from collections import deque

chat_history = deque(maxlen=100)  # Keeps only the last 100 messages

# Load chat history
def load_chat():
    global chat_history
    try:
        with open("./mybot/chat_history2.json", "r") as f:
            chat_history.extend(json.load(f))  # Load into deque or list
    except FileNotFoundError:
        pass  # No chat history yet

def add_message(sender, message):
    chat_history.append({"sender": sender, "message": message})

# Save chat history
def save_chat():
    with open("./mybot/chat_history2.json", "w") as f:
        json.dump(list(chat_history), f, indent=4)  # Convert deque to list before saving

# def print_hello():
#     print("Hi Linda!!!!!")

# # Use the functions
# load_chat()
# add_message("user", "What's the weather today?")
# add_message("bot", "It's sunny with a high of 75°F.")
# save_chat()

# # Print chat history
# for entry in chat_history:
#     print(f"[{entry['sender'].upper()}]: {entry['message']}")