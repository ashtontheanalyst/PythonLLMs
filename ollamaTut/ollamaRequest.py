# This is extremely similar to 'manualRequest.py' but it's cleaned up code,
# also doesn't have the streaming mode which would be nice

from ollama import chat, Client

# Init the ollama client
client = Client()

# Set the model and the prompt
# NOTE: If you made your own tweaked model you can use it here too
# model = "llama3.1"
model = "jane"
prompt = input("What do you want to ask?:\n")

# Send the query to the model
print("\nThinking...")
response = client.generate(model=model, prompt=prompt)

# Print the models response
print("Response from Llama 3.1:")
print(response.response)
print("\nComplete")