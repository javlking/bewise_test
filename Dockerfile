FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /quiz

COPY . /quiz

RUN pip install -r requirements.txt
