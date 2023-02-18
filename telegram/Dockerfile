FROM continuumio/miniconda3

# install cv2 dependencies
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

RUN conda update --all
RUN conda install pip
RUN conda install -c conda-forge opencv

RUN mkdir \app
ADD src /app
ADD requirements.txt /app
ADD .env /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD python /app/main.py
