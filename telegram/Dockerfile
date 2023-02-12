FROM python:3.9.6

RUN pip install --upgrade pip\
    && mkdir \app

# install cv2 dependencies
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

ADD src /app
ADD requirements.txt /app
ADD .env /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD python /app/main.py