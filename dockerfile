FROM python:3.9-slim

WORKDIR /app

COPY . /app/


RUN pip install --upgrade pip

RUN apt-get update -y && apt-get install -y gcc

RUN pip install discordbot.py

RUN pip install SQLAlchemy

RUN pip install psycopg2-binary

RUN pip install requests

RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*

RUN  apt-get update \
  && apt-get install -y un \
  && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/JaidedAI/EasyOCR/releases/download/v1.3/english_g2.zip
RUN wget https://github.com/JaidedAI/EasyOCR/releases/download/pre-v1.1.6/craft_mlt_25k.zip
RUN mkdir ~/.EasyOCR
RUN mkdir ~/.EasyOCR/model
RUN unzip english_g2.zip -d ~/.EasyOCR/model
RUN unzip craft_mlt_25k.zip -d ~/.EasyOCR/model

EXPOSE 5050

CMD ["python", "dragonbot.py"]