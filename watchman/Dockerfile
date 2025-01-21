FROM condaforge/miniforge3

ARG DEBIAN_FRONTEND=noninteractive

# install cv2 dependencies
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

RUN conda update --all
RUN conda install pip
RUN conda install -c conda-forge opencv

RUN mkdir \app
COPY watchman/src /app
COPY watchman/requirements.txt /app
COPY /shared /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD python /app/main.py
