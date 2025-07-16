FROM python:3.11-slim

WORKDIR /app

# Move my local requirements.txt to the container and install
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# If all if well, run the app, reload when I make a change
CMD fastapi run --reload