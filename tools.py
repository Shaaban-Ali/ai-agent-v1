def analyze_text(text: str):
    words = text.split()
    length = len(words)
    return {
        "word_count": length,
        "preview": " ".join(words[:10])
    }

def execute_math(expression: str):
    try:
        result = eval(expression)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}
