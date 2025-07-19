import ollama
import time
import os
import json

# The peter-pan file has weird line breaks in the sentences so we're putting
# them into propoer paragraphs
def parseFile(filename):
    with open(filename, encoding="utf-8-sig") as f:
        paragraphs = []
        buffer = []         # Append each string to this then push to para

        # Go line for line through our file
        for line in f.readlines():
            line = line.strip()

            # If it's a true line of text, put it in the buffer
            # If we hit a newline, append all text lines from the buffer into
            # the paragraph and then empty the buffer for follow on lines
            if line:
                buffer.append(line)
            elif len(buffer):
                paragraphs.append((" ").join(buffer))
                buffer = []
        
        # Last buffer check
        if len(buffer):
            paragraphs.append((" ").join(buffer))
        return paragraphs


# This saves our embeddings for a specific file since it takes so long
def saveEmbeddings(filename, embeddings):
    # Create a dir if it doesn't exist
    if not os.path.exists("embeddings"):
        os.makedirs("embeddings")

    # dump embeddings to a specific json file of the filename
    # So in the test case we'd have a peter-pan.json filled with embeddings
    with open(f"embeddings/{filename}.json", "w") as f:
        json.dump(embeddings, f)


# Load in the embeddings from a save
def loadEmbeddings(filename):
    # Check if the file exists, based on creation from saveEmbeddings()
    if not os.path.exists(f"embeddings/{filename}.json"):
        return False
    
    # If it does then parse the json back
    with open(f"embeddings/{filename}.json", "r") as f:
        return json.load(f)


# Main embeddings function
def getEmbeddings(filename, modelname, chunks):
    # Check to see if they already exist, try to load in if possible
    if (embeddings := loadEmbeddings(filename)) is not False:
        return embeddings
    
    # Otherwise... get the embeddings and save them (generate)
    embeddings = [
        ollama.embeddings(model=modelname, prompt=chunk)["embedding"]
        for chunk in chunks
    ]

    # Save the embeddings
    saveEmbeddings(filename, embeddings)
    return embeddings


def main():
    # Open the file
    filename = "peter-pan.txt"

    # Fix our data from the txt file
    paragraphs = parseFile(filename)

    # Time the embeddings
    start = time.perf_counter()

    # Do the embeddings, show how many we have
    embeddings = getEmbeddings(filename, "llama3.1", paragraphs)
    print(time.perf_counter() - start)
    print(len(embeddings))
    


if __name__ == "__main__":
    main()