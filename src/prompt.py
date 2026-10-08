from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

contextualize_q_prompt = ChatPromptTemplate.from_messages([
    ("system", "Rewrite the user's question using the chat history when needed."),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
])

system_prompt = """
You are a helpful Medical Assistant.

Use the retrieved medical context to answer the user's question.

Use the chat history to understand previous messages and remember
information the user has already provided, such as their name.

If you don't know the answer, say you don't know.

Keep your answer within three to five sentences maximum to keep the answer precise.
Context : {context}
"""

qa_prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
])