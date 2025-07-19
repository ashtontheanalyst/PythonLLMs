import requests
from flask import Flask, Response, request, render_template

# Init the app
app = Flask(__name__)


# Home page of the app
@app.route("/")
def home():
    return render_template('home.html')


# Prompting endpoint
@app.route("/ask")
def ask():
    prompt = request.args.get("prompt")
    if not prompt:
        return Response('{"error": "No prompt provided"}', mimetype="application/json")

    # Reach out to our local Ollama LLM via the endppint API with our prompt
    response = requests.post('http://ollama:11434/api/generate', json={
        "prompt": prompt,
        # True makes it look like chatGPT where it comes in word by word, but
        # it sends a separate json packet each time so don't do that
        "stream": False,
        "model": "thor"
    })

    return Response(response.text, mimetype="application/json", status=response.status_code)


# Runs the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)