import json
from collections import deque


# Load chat history
def load_chat():
    # global chat_history
    try:
        with open("./mybot/chat_history.json", "r") as f:
            chat_history = deque(json.load(f), maxlen=5)
            return chat_history
    except FileNotFoundError:
        print("No Chat History Found")
        pass  # No chat history yet

def add_message(chat_history, sender, message):
    chat_history.append({"role": sender, "content": message})

# Save chat history
def save_chat(chat_history):
    with open("./mybot/chat_history.json", "w") as f:
        json.dump(list(chat_history), f, indent=4)  # Convert deque to list before saving

