# This will connect to ollama running in the background, our specific model
# and then return the answer to us. Think of it like a small, local, ChatGPT
# in our terminal

# So, make sure ollama is downloaded, llama 3.1 is there, and then run
# ollama serve, then run this python script

import requests
import json

# Set the base URL for the locally hosted Ollama 3.1 8B API
url = "http://localhost:11434/api/chat"

# Define your payload, the input prompt
payload = {
    "model": "llama3.1",
    "messages": [{"role": "user", "content": "Tell me something interesting please!"}]
}

# Send an HTTP POST req. to the api endpoint
# Stream grabs the responses from the LLM in real time, shows it typing
response = requests.post(url, json=payload, stream=True)

# If we get a good connection, print out each line
if response.status_code == 200:
    print("Streaming response from Llama 3.1:")
    for line in response.iter_lines(decode_unicode=True):
        if line:    # Ignores empty lines
            try:
                # Parse each line from JSON
                json_data = json.loads(line)
                
                # Extract and print the message
                if "message" in json_data and "content" in json_data["message"]:
                    print(json_data["message"]["content"], end="")
            except json.JSONDecodeError:
                print(f"\nFailed to parse this line: '{line}'")
    print("\n\nEND OF MESSAGE")
else:
    print(f"ERROR: {response.status_code}")
    print(response.text)