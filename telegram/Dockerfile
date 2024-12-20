FROM python:latest

RUN mkdir \app
COPY telegram/src /app
COPY telegram/requirements.txt /app
COPY telegram/.env /app
COPY /shared /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD python /app/main.py
