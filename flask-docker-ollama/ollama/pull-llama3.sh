set -e

./bin/ollama serve &

pid=$!

sleep 5

echo "Pulling llama3 model"
ollama pull llama3

# Customizing llama3.1 from the Modelfile
# From llama3, make THOR (Technical Helper with Optimized Responses)
echo "Creating THOR..."
ollama create thor -f /Modelfile

wait $pid