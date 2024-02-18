FROM python:3.9-slim

WORKDIR /app

COPY . /app/


RUN pip install --upgrade pip

RUN apt-get update -y && apt-get install -y gcc

RUN pip install discordbot.py

RUN pip install SQLAlchemy

RUN pip install psycopg2-binary

RUN pip install requests

RUN pip install easyocr

EXPOSE 5050

CMD ["python", "dragonbot.py"]