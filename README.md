# End-to-End-Medical-Chatbot

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Framework](https://img.shields.io/badge/framework-FastAPI-009688.svg?logo=fastapi&logoColor=white)
![LLM](https://img.shields.io/badge/LLM-Groq-F55036.svg?logo=groq&logoColor=white)
![Vector DB](https://img.shields.io/badge/VectorDB-Pinecone-000000.svg?logoColor=white)

</div>

---

## 🎯 Overview

**End-to-End Medical Chatbot** is an AI-powered medical assistant built with **Retrieval-Augmented Generation (RAG)** to provide accurate, context-aware medical information grounded in a medical knowledge base. Powered by **FastAPI** on the backend, it features an interactive, user-friendly chat interface and a conversational memory system that retains chat history to deliver more relevant, continuous responses across interactions.

---

## 📸 Application Preview

<p align="center">
  <img src="image\frontend_demo.png" alt="Medical Chatbot Interface" width="85%" />
</p>

---

### Key Highlights

✅ **RAG-Powered** : Retrieves relevant medical context before generating responses  
✅ **Poduction-Ready** : Fully containerized with CI/CD pipeline  
✅ **Scalable Retrieval** : Powered by Pinecone for efficient, high-performance vector search  
✅ **AI-Powered Responses** : Leverages Groq's fast LLM inference for responsive, context-aware medical conversations  
✅ **Conversational Memory** : Retains chat history to maintain context and provide more coherent follow-up responses 

✅ **Automated Deployment** : Streamlined Docker containerization and GitHub Actions CI/CD pipeline

---

## ✨ Features

- 🤖 **Smart Q&A** : Context-aware medical question answering using RAG
- 📚 **PDF Knowledge Base** : Automatic ingestion and processing of medical documents
- ⚡ **Vector Search** : Efficient similarity search powered by Pinecone
- 🧠 **Advanced LLM** : Groq for high-quality natural language generation
- 🎨 **User-Friendly Interface** : Intuitive web chat UI with real-time responses
- 🔒 **Environment-Based Config** : Secure credential management via `.env`
- 🐳 **Docker Support** : Containerized deployment for consistency
- 🚀 **CI/CD Pipeline** : Automated deployment to AWS via GitHub Actions
- 📝 **Comprehensive Docs** : Full documentation and architecture guides

---

## 🏗️ Architecture

### System Overview

The chatbot follows a classic RAG architecture pattern:

```
┌─────────────────────────────────────────────────────────────┐
│                   Medical Chatbot System                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │           User Interface (FastAPI Web App)           │   │
│  │  • HTML/CSS/JavaScript Chat Interface                │   │
│  │  • Real-time Response Display                        |   |
|  |  • Chat History Retain                               │   │   
│  └──────────────┬───────────────────────────────────────┘   │
│                 │                                           │
│  ┌──────────────▼───────────────────────────────────────┐   │
│  │         FastAPI Backend (app.py)                     │   │
│  │  • Route Handlers (/chat, /)                         │   │
│  │  • Request Validation                                │   │
│  └──────────────┬───────────────────────────────────────┘   │
│                 │                                           │
│  ┌──────────────▼───────────────────────────────────────┐   │
│  │      LangChain RAG Pipeline                          │   │
│  │  • Retrieval Chain                                   │   │
│  │  • Document Combination                              │   │
│  │  • Prompt Management                                 │   │
│  └──────────────┬───────────────────────────────────────┘   │
│                 │                                           │
│    ┌────────────┴──────────────┬──────────────┐             │
│    │                           │              │             │
│  ┌─▼──────────┐          ┌─────▼─┐    ┌───────▼────┐        │
│  │ Pinecone   │          │ Groq  │    │ HuggingFace│        │
│  │ Vector DB  │          │  LLM  │    │ Embeddings │        │
│  └────────────┘          └───────┘    └────────────┘        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
End-to-End-Medical-Chatbot/
│
├── .github/
│   └── workflows/
│       └── cicd.yaml              # CI/CD workflow
│
├── data/
│   └── Medical_book.pdf           # Medical knowledge source
│
├── image/
|    └── frontend_demo.png
├── research/
│   └── notebook.ipynb             # Experiments and exploration
│
├── src/
│   ├── __init__.py
│   ├── chat_history.py             # Conversational memory
│   ├── helper.py                   # Helper functions
│   └── prompt.py                   # Prompt templates
│
├── static/
│   └── style.css                   # Frontend styling
│
├── templates/
│   └── chat.html                   # Chat interface
│
├── .dockerignore
├── .env.example                    # Environment template
├── .gitignore
├── app.py                          # Application entry point
├── Dockerfile                      # Docker configuration
├── requirements.txt                # Python dependencies
├── setup.py                        # Package configuration
├── store_index.py                  # Vector indexing pipeline
├── template.sh                     # Project setup script
├── LICENSE
└── README.md
```

---

## 🚀 Installation

### Prerequisites

Before you begin, ensure you have the following:

- **Python 3.12+** installed
- **API Keys**:
  - [Groq API Key](https://console.groq.com/keys)
  - [Pinecone API Key](https://www.pinecone.io/)

Optional for faster setup:
- **UV Package Manager**

### Using Conda (Recommended)

Conda is well-tested and widely used in the ML/AI community.

#### Step 1 : Clone the repositiry

```bash
git clone https://github.com/Rifat211-debug/End-to-End-Medical-Chatbot
cd End-to-End-Medical-Chatbot
```

#### Step 2: Create Conda Environment

```bash
conda create -n medibot python=3.12 -y
conda activate medibot
```

#### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

#### Step 4: Configure Environment Variables

Create a `.env` file in the root directory:

```bash
# .env
PINECONE_API_KEY="your_pinecone_api_key_here"
GROQ_API_KEY="your_groq_api_key_here"
```

#### Step 5: Index Medical Documents

Place your medical PDF files in the `data/` directory, then run:

```bash
python store_index.py
```

This will:
- Load all PDFs from `data/` directory
- Split text into chunks (500 chars with 20 char overlap)
- Generate embeddings using HuggingFace model
- Upload to Pinecone vector database

#### Step 6: Run the Application

```bash
uvicorn app:app --reload --port 8080
```

The application will start at `http://localhost:8080`

---

### Using UV (Faster Alternative)

UV is significantly faster for dependency resolution and installation (~10x faster than pip).

#### Step 1-2: Clone and Navigate

```bash
git clone https://github.com/Rifat211-debug/End-to-End-Medical-Chatbot
cd End-to-End-Medical-Chatbot
```

#### Step 3: Create Virtual Environment with UV

```bash
# Create and activate a UV-managed Python environment
uv venv --python 3.12 .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

#### Step 4: Install Dependencies with UV

```bash
uv pip install -r requirements.txt
```

#### Step 5-6: Configure and Run

Follow the same environment configuration and running steps as above (Steps 4-6 from Conda section).

**Why UV?**
- ⚡ **10x faster** dependency resolution
- 📦 **Simpler syntax** than pip
- 🔒 **Better lock files** for reproducibility
- 🎯 **Drop-in replacement** for pip

---

## 💬 Usage

### Web Interface

Once the application is running at `http://localhost:8080`:

1. **Open your browser** and navigate to `http://localhost:8080`
2. **Type your medical query** in the chat input box
3. **Press Enter** or click Send
4. **Receive AI-generated response** based on your knowledge base

### Example Queries

```
- "What are the symptoms of diabetes?"
- "How is hypertension treated?"
- "Explain the causes of heart disease"
```

### Programmatic Usage

```python
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI

# Initialize components
embeddings = download_hugging_face_embeddings()
docsearch = PineconeVectorStore.from_existing_index(
    index_name="medical-chatbot",
    embedding=embeddings
)

# Query the system
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})
# Use retriever for custom implementations
```

---

## 🔌 API Endpoints

### GET `/`

Returns the chat interface HTML page.

**Response**: HTML chat UI

---

### POST `/chat`

Processes user queries and returns AI-generated responses.

**Request Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `msg` | string | Yes | User's medical query |

**Example Request:**

```bash
curl -X POST http://localhost:8080/get \
  -d "msg=What are the symptoms of diabetes?"
```

**Example Response:**

```
Diabetes symptoms include increased thirst, frequent urination, fatigue, 
and blurred vision. More serious symptoms may include slow wound healing, 
tingling in the extremities, and recurring infections.
```

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Language** | Python 3.12+ | Core Programming Language |
| **Web Framework** | FastAPI | Web server and routing |
| **LLM Orchestration** | LangChain | RAG pipeline management |
| **Large Language Model** | Groq | Natural language generation |
| **Vector Database** | Pinecone | Semantic search and embedding storage |
| **Embeddings** | HuggingFace (all-MiniLM-L6-v2) | Text-to-vector conversion (384-dim) |
| **PDF Processing** | PyPDF2 | PDF document parsing |
| **Environment Config** | python-dotenv | Secure credential management |
| **Frontend** | HTML/CSS/JavaScript | User chat interface |
| **Containerization** | Docker | Application containerization |
| **CI/CD** | GitHub Actions | Automated deployment pipeline |
| **Deployment** | AWS (EC2, ECR) | Cloud infrastructure |

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Salauddin Al Rifat**
- Email: salauddin.alrifat@gmail.com
- GitHub: [@Rifat211-debug](https://github.com/Rifat211-debug)

---

## ⭐ Acknowledgments

- GROQ for the LLM Model
- Pinecone for vector database infrastructure
- LangChain for RAG orchestration framework
- HuggingFace for embedding models

---

<div align="center">

**Made with ❤️ for the healthcare community**

⭐ If this project helps you, please consider giving it a star!

</div>



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_DEFAULT_REGION
   - ECR_REPO
   - PINECONE_API_KEY
   - GROQ_API_KEY
