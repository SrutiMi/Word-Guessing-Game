FROM python:3.10.6

WORKDIR /app
COPY . /app/

RUN apt-get update && apt-get install -y python3.10

CMD [ "python", "game.py" ]