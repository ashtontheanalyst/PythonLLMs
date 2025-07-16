# The main Fast API application
from fastapi import FastAPI, Response
import requests

# Create an instance of the FastAPI class
app = FastAPI()

# Endpoint for prompting
@app.get('/ask')
def ask(prompt :str):
    # Reach out to our local Ollama LLM via the endppint API with our prompt
    response = requests.post('http://ollama:11434/api/generate', json={
        "prompt": prompt,
        # True makes it look like chatGPT where it comes in word by word, but
        # it sends a separate json packet each time so don't do that
        "stream": False,
        "model": "llama3"
    })

    return Response(content=response.text, media_type="application/json")