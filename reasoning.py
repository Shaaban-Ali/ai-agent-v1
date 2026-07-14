def think(text: str):
    steps = [
        "1. Understand the question.",
        "2. Identify key terms.",
        "3. Determine the user's intent.",
        "4. Produce a logical conclusion."
    ]

    return {
        "steps": steps,
        "conclusion": f"After analysis, the message appears to be about: {text}"
    }
