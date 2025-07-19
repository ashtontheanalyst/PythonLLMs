# Input a prompt from the command line while the services (flask and ollama
# Docker containers) are up, and get the response from the LLM
import requests
import json

# Start up info
print("------------------------- LOCALLY HOSTED LLM -------------------------\n" \
      "DC 1: Docker container 1 hosts a python slim image running Flask. This\n" \
      "      is the api endpoint for our local LLM which recieves the prompt.\n\n" \
      "DC 2: Docker container 2 hosts an ollama image which loads in the\n" \
      "      Llama 3.1 LLM with 8B param.'s. There's also a Makerfile to edit\n" \
      "      the models behavior at SYSTEM level, it's called 'THOR'.\n" \
)

print("----------------------------- PROMPTING ------------------------------")
while True:
    prompt = input("INPUT (q to quit): \n")

    # Empty prompt or entered quit to break loop
    if not prompt:
        print("[ERR: Enter a real prompt...]\n\n")
    elif prompt == "q" or prompt == "Q":
        break

    # If they did enter a prompt, run it to the ollama backend to return a response
    elif prompt:
        print("\nLoading, please wait..\n")

        # This is the full JSON response from the LLM api
        response = requests.get(f'http://localhost:5000/ask?prompt={prompt}').text

        # Parse the JSON to get what we want
        parsed = json.loads(response)
        parsed = parsed["response"]
        print(f"RESPONSE:\n{parsed}\n")