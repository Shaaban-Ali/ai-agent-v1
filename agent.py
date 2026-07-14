from tools import analyze_text, execute_math
from reasoning import think
from transformers import pipeline

ai_model = pipeline("sentiment-analysis")

def agent_brain(message: str):
    if any(op in message for op in ["+", "-", "*", "/"]):
        return {
            "mode": "execution",
            "result": execute_math(message)
        }

    if len(message.split()) > 10:
        return {
            "mode": "analysis",
            "result": analyze_text(message)
        }

    if "why" in message.lower() or "?" in message:
        return {
            "mode": "reasoning",
            "result": think(message)
        }

    result = ai_model(message)[0]
    return {
        "mode": "ai",
        "result": result
    }
