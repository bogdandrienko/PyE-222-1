FROM python:3.11
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /web
WORKDIR /web

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
