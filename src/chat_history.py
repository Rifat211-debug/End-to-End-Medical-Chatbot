from langchain_core.messages import AIMessage, HumanMessage

# Store conversation hostory
chat_history = []

def add_user_message(message : str):
    chat_history.append(
        HumanMessage(content = message)
    )

def add_ai_message(message : str):
    chat_history.append(
        AIMessage(content = message)
    )    

def get_chat_history():
    return chat_history

def clear_chat_history():
    chat_history.clear()