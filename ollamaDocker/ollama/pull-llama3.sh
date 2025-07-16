set -e

./bin/ollama serve &

pid=$!

sleep 5

echo "Pulling llama3 model"
ollama pull llama3

# From llama3, make jean grey
echo "Creating Jean Grey model..."
ollama create jean-grey -f /Modelfile

wait $pid