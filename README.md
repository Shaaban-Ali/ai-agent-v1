# AI Agent v1

**AI Agent v1** is the first experimental version of a simple AI agent built using Python and FastAPI, with a lightweight web interface (HTML/CSS/JS).  
The goal of this initial version is to establish a clear agent architecture with basic tools, short-term memory, simple reasoning, and basic text-processing capabilities.

This version serves as the foundation for future, more advanced AI agent systems.

---

## 🚀 Features (v1)

### 1. FastAPI Backend
- Single endpoint `/chat`
- Receives user messages and returns agent responses
- Simple structure, easy to extend in future versions

### 2. Lightweight Web Frontend
- Clean chat interface
- Built with HTML + CSS + JavaScript
- Sends messages to the API and displays responses instantly

### 3. Basic AI Agent
The agent includes:
- **Short-term memory** to store recent messages
- **Simple tools**, including:
  - Sentiment analysis
  - Basic math operations
  - Text analysis
- **Simple reasoning** to decide which tool to use based on the user’s message

### 4. Clear Project Structure
```
ai-agent-v1/
│
├── agent.py        # Core agent logic
├── tools.py        # Tools (Math, Sentiment, Text)
├── memory.py       # Short-term memory
├── reasoning.py    # Tool selection logic
├── main.py         # FastAPI backend
│
└── frontend/       # Web interface
    ├── index.html
    ├── styles.css
    └── script.js
```

---

## 🎯 Purpose of v1

This version is not meant to be a fully intelligent agent.  
It is:

- A **prototype**
- A starting point for building an AI agent from scratch
- A demonstration of:
  - Tools
  - Memory
  - Reasoning
  - Web + API integration

The main goal is to build the **correct foundation** before adding real intelligence.

---

## 🛠️ How the Agent Works

1. User sends a message from the web interface  
2. FastAPI receives the message  
3. The agent analyzes the message:
   - Numbers → Math tool  
   - Emotional text → Sentiment tool  
   - General text → Text analysis tool  
4. The message is stored in memory  
5. The response is returned to the frontend  

---

## 📌 Example

**User:**  
> Calculate 12 + 8

**Agent:**  
> The result is 20

---

## 📦 Requirements

- Python 3.10+
- FastAPI
- Uvicorn

Install dependencies:

```bash
pip install fastapi uvicorn
```

Run the server:

```bash
uvicorn main:app --reload
```

---

## 📄 Notes (v1)

- This version is intentionally simple  
- No real AI model yet  
- Future versions will include:
  - LLM integration
  - Long-term memory
  - Advanced tools
  - Plugin system
  - State management
  - Task execution

---

## 📚 Future Plans (v2)

Version 2 will include:
- Real AI model integration
- Improved UI
- More intelligent tools
- Better reasoning and memory
- Support for long conversations

---

## 👤 Developer

**Shaaban Ali**  
AI Engineer passionate about building practical and scalable AI systems.

---

## ⭐ Thank you for using AI Agent v1  
This is only the beginning — more powerful versions are coming soon.
