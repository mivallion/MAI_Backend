FROM python:3.7-alpine

WORKDIR /app

RUN apk update \
    && apk add gcc python3-dev musl-dev
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
