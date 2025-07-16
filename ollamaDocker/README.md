# Ollama on Docker with FastAPI
https://www.youtube.com/watch?v=0c96PQd3nA8&t=937s


## Notes:
- (DONE) Get this container a Modelfile to act like Jane Grey from X-Men, see
`ollamaTut` for more help.
- Make this a RAG with some sort of safe and small data file, from there we
can expand it to use the MITRE ATT&CK framework.


## Install/Setup
1. Dowload Docker - look it up, kind of a lot of steps

2. Download Ollama and make sure Ollama3.1 is installed on host/docker 
machine. See `ollamaTut` for more info and help.

3. Create a virtual env and/or get into it:
```sh
python3 -m venv fastenv
source fastenv/bin/activate
```

4. Download Req's (inside fastenv):
```sh
pip install -r /fastapi/requirements.txt
```


## Build Docker Container
1. Confirm you're in the `ollamaDocker` top directory
2. Build the container and start it:
```sh
sudo docker compose up --build
```
3. Wait a super long time for the container to build, then wait longer
for ollama to download ollama 3.1 into the container
    - If you get concerned that nothing is happening, open another container
    and navigate to the same directory then enter:
    ```sh
    docker compose logs -f ollama
    ```
    - Now look in the bottom corner and it'll show you a time

4. Starting it up from here on it is the same command as building. Just
visit http://0.0.0.0:8000/docs once it's spun up and you should see the GUI.