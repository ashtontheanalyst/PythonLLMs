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
Create a python local env and get into it:
```sh
python -m venv oenv
source oenv/bin/activate
```

#### The following will take decent time:
Download ollama in oenv (requires int once):
```sh
curl -fsSL https://ollama.com/install.sh | sh
```

Download the LLM model in oenv (requries int once):
```sh
# This is Ollama 3.1 with 8 Billion Param's
ollama run ollama3.1
```

Commands for the model:
```sh
# To start the model up run the same command as for downloading (int. not req.)
ollama run ollama3.1

/?      # Show commands
/bye    # Exit the prompting

# Starts an ollama server in the background
ollama serve
```

## Modify Model with a Modelfile
A modelfile allows us to tweak and change the base LLM to do specific things. First thing is to make a Modelfile in the directory and write in it.
<br><br>

Create a new model in ollama:
```sh
ollama create newNametoGiveLLM -f ./Modelfile
```

Once that's done then you have a working model with tweaks!