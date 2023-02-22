FROM python:latest

RUN mkdir \app
ADD src /app
ADD requirements.txt /app
ADD .env /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD python /app/main.py
