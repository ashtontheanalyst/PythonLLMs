# Ollama Tutorial

### Links:
Tutorial: https://www.youtube.com/watch?v=UtSSMs6ObqY&t=629s  
Ollama Github: https://github.com/ollama/ollama  
Ollama Docker Image: https://hub.docker.com/r/ollama/ollama  

### Notes:
- Hosts a local LLM model (TARGET is 'Model: Llama 3.1, Param: 8B, Size: 4.7Gb). 
- We also created our own tweaked version of Llama 3.1 that is instructed
to act like Jane Grey from X-Men, it's called 'jane'.
- When you download an LLM, it only pulls from internet that one time. From
there, any requests, queries, or etc. will be pulled from the LLM that is
hosted locally from that download.
- Has an official image on Docker for use cases in the future
- Spins up an HTTP server that can be used to call out to via API calls
- Python native

## Install/Setup:
1. Create a python local env and get into it:
```sh
python -m venv oenv
source oenv/bin/activate
```

2. Download ollama in oenv (requires int once):
```sh
curl -fsSL https://ollama.com/install.sh | sh
```

3. Download the LLM model in oenv (requries int once):
```sh
# This is Ollama 3.1 with 8 Billion Param's
ollama run ollama3.1
```

## Running the Scripts:
- `manualRequest.py` once run will send a PRE-MADE prompt to the Llama3.1 8B model
and stream back it's response in the terminal
- `ollamaRequest.py` does something very similar but it allows us to tweak the
prompt in the terminal before it's sent off. Doesn't stream in the response.  

1. Run the ```sh ollama serve``` command to get Ollama running in the background of
one terminal
2. In another terminal, navigate to the `basic-ollama/` directory and then run either
of the scripts like: ```sh python3 manualRequest.py```

## Commands for the model:
```sh
# To start the model up run the same command as for downloading (int. not req.)
ollama run ollama3.1

/?      # Show commands
/bye    # Exit the prompting

# Starts an ollama server in the background, needed before running
# manualRequest.py and ollamaRequest.py
ollama serve
```