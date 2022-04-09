FROM python:3.8.6-slim-buster

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/
COPY ./src /app/src

ENV PYTHONPATH /app
CMD python src/server.py
WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip==22.0.4 \
    && pip install -r requirements.txt \
    && rm -rf /root/.cache/*
