import os
from dotenv import load_dotenv

load_dotenv()

# === 🔐 API Keys ===
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

# === 🧠 Embedding / LLM Settings ===
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "HuggingFaceH4/zephyr-7b-alpha"  # or any other LLM if needed              

# === 📦 Qdrant Settings ===
QDRANT_PORT = 443
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY") 
QDRANT_HOST = os.getenv("QDRANT_HOST")        
QDRANT_COLLECTIONS = [                        
    "Enterprise_flat",
    "Enterprise_hnsw",
    "Enterprise_quantized"
]

# === ✂️ Chunking Settings ===
CHUNK_SIZE = 800
CHUNK_OVERLAP = 100

# === 📁 Paths ===
DATA_DIR = "data"
OUTPUT_DIR = "outputs"
DOCX_OUTPUT_PATH = os.path.join(OUTPUT_DIR, "rag_output.docx")

# === 🔎 LangSmith Config ===
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT", "productivity-rag")
LANGCHAIN_ENDPOINT = os.getenv("LANGCHAIN_ENDPOINT", "https://api.smith.langchain.com")
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2", "true").lower() == "true"

# === LangSmith Client ===
from langsmith import Client
langsmith_client = Client(api_key=LANGCHAIN_API_KEY)
