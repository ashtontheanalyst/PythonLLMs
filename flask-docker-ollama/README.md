# Docker Containers Hosting Flask and Ollama LLM

## Notes:
- Flask is the API enpoint for sending the prompt to, it then sends it to the 
Ollama container to generate a response, then send it back to the user.
- Docker container 1 hosts a python slim image running Flask. This
is the api endpoint for our local LLM which recieves the prompt. It lso will host
the web app once it's complete.
- Docker container 2 hosts an ollama image which loads in the Llama 3.1 LLM with 
8B param.'s. There's also a Makerfile to edit the models behavior at SYSTEM level, 
it's called 'THOR'.
- (IN-PROG.) Flask also hosts a web service that allows us to see an application 
that looks somewhat similar to chatGPT or other chat engines.


## Install/Setup:
1. Create and source into a virtual env
```sh
python -m venv ragenv
source ragenv/bin/activate
```
2. Download necessary dependencies in `requirements.txt`
```sh
pip install -r requirements.txt
```
3. Stand up the containers from the compose file:
```sh
sudo docker compose up --build
```
4. In another terminal, get back to this directory and into the venv.
5. To run the Command Line Tool for prompting the model:
```sh
python3 prompt.py
```