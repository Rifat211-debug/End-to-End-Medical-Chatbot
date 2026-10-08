from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from langchain_pinecone import PineconeVectorStore
from langchain.chains import create_retrieval_chain, create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_groq import ChatGroq

from src.helper import download_hugging_face_embeddings
from src.prompt import contextualize_q_prompt, qa_prompt
from src.chat_history import get_chat_history, add_ai_message, add_user_message

import os
from dotenv import load_dotenv

# ============================================================
# APP SETUP
# ============================================================

app = FastAPI()
load_dotenv()

# ============================================================
# API KEYS
# ============================================================

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# ============================================================
# TEMPLATES + STATIC FILES
# ============================================================

templates = Jinja2Templates(directory = "templates")
app.mount(
    "/static",
    StaticFiles(directory = "static"),
    name = "static"
)

# ============================================================
# EMBEDDINGS & PINECONE
# ============================================================

embeddings = download_hugging_face_embeddings()

index_name = "medical-chatbot"
docsearch = PineconeVectorStore.from_existing_index(
    index_name = index_name,
    embedding = embeddings
)

# ============================================================
# RETRIEVER
# ============================================================

retriever = docsearch.as_retriever(
    search_type = "similarity",
    search_kwargs = {"k" : 3}
)

# ============================================================
# GROQ CHAT MODEL
# ============================================================

ChatModel = ChatGroq(model = "openai/gpt-oss-120b", temperature = 0)

# ============================================================
# ALL THE CHAINs
# ============================================================

history_aware_retriever = create_history_aware_retriever(
    ChatModel,
    retriever,
    contextualize_q_prompt
)

question_answer_chain = create_stuff_documents_chain(
    ChatModel,
    qa_prompt
)

rag_chain = create_retrieval_chain(
    history_aware_retriever,
    question_answer_chain
)


# ============================================================
# HOME PAGE
# ============================================================

@app.get("/", response_class = HTMLResponse)
async def index(request : Request):
    return templates.TemplateResponse(
       request = request,
       name = "chat.html"
    )

# ============================================================
# CHAT
# ============================================================

@app.post("/chat")
async def chat(msg : str = Form(...)):

    print("User : ", msg)

    history = get_chat_history()
    response = rag_chain.invoke({
        "input" : msg,
        "chat_history" : history
        })

    answer = response["answer"]
    print("Response : ", answer)

    add_user_message(msg)

    add_ai_message(answer)

    return answer


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host = "0.0.0.0", port = 8080)
