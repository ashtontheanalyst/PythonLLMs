set -e

./bin/ollama serve &

pid=$!

sleep 5

echo "Pulling llama3 model"
ollama pull llama3

# From llama3, make Batman
echo "Creating Batman model..."
ollama create batman -f /Modelfile

wait $pid