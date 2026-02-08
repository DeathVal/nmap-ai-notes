import os

def improve_with_ai(markdown, parsed):
    if not os.getenv("OPENAI_API_KEY"):
        return markdown
    return markdown
