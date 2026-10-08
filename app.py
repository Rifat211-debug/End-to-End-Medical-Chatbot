from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

app = FastAPI()

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

templates = Jinja2Templates(directory = "templates")
app.mount(
    "/static",
    StaticFiles(directory = "static"),
    name = "static"
)


embeddings = download_hugging_face_embeddings()

index_name = "medical-chatbot"

# Connect to the existing Pinecone index
docsearch = PineconeVectorStore.from_existing_index(
    index_name = index_name,
    embedding = embeddings
)

retriever = docsearch.as_retriever(
    search_type = "similarity",
    search_kwargs = {"k" : 3}
)

ChatModel = ChatGroq(model = "openai/gpt-oss-120b", temperature = 0)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

question_answer_chain = create_stuff_documents_chain(
    ChatModel,
    prompt
)

rag_chain = create_retrieval_chain(
    retriever,
    question_answer_chain
)


@app.get("/", response_class = HTMLResponse)
async def index(request : Request):
    return templates.TemplateResponse(
       request = request,
       name = "chat.html"
    )

@app.post("/chat")
async def chat(msg : str = Form(...)):
    input = msg
    print(input)

    response = rag_chain.invoke({"input" : msg})

    print("Response : ", response["answer"])

    return response["answer"]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host = "0.0.0.0", port = 8080)
