from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from memory import AgentMemory
from tools import analyze_text, execute_math
from reasoning import think
from agent import agent_brain   # Important core agent logic

# ---------------------------
# Initialize FastAPI application
# ---------------------------
app = FastAPI()

# ---------------------------
# CORS configuration (fixes 405 OPTIONS issue)
# ---------------------------
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],          # GET, POST, OPTIONS...
    allow_headers=["*"],          # Allow all headers
)

# ---------------------------
# AI model (Sentiment Analysis)
# ---------------------------
ai_model = pipeline("sentiment-analysis")

# ---------------------------
# Memory system
# ---------------------------
memory = AgentMemory()

class ChatMessage(BaseModel):
    message: str

# ---------------------------
# Endpoints
# ---------------------------

@app.get("/")
def home():
    return {"message": "AI Agent is running!"}

@app.post("/chat")
def chat(data: ChatMessage):
    memory.add(data.message)
    result = ai_model(data.message)[0]
    return {
        "input": data.message,
        "label": result["label"],
        "score": result["score"],
        "memory": memory.get()
    }

@app.post("/analyze")
def analyze(data: ChatMessage):
    result = analyze_text(data.message)
    return {
        "input": data.message,
        "analysis": result
    }

@app.post("/reason")
def reason(data: ChatMessage):
    result = think(data.message)
    return {
        "input": data.message,
        "reasoning": result
    }

@app.post("/execute")
def execute(data: ChatMessage):
    result = execute_math(data.message)
    return {
        "input": data.message,
        "execution": result
    }

# ---------------------------
# Main AI Agent endpoint
# ---------------------------
@app.post("/agent")
def agent_endpoint(data: ChatMessage):
    result = agent_brain(data.message)
    return {
        "input": data.message,
        "mode_used": result["mode"],
        "output": result["result"]
    }
