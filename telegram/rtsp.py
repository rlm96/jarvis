import cv2
import time
import os
from datetime import datetime

base_address = "rtsp://{user}:{password}@{ip}/{url_path}"
video_extension = '.mp4'
video_base_path = 'media'

class Stream:
    def __init__(self, ip, user, password, url_path):
        self.url_address = base_address.format(ip=ip, user=user, password=password, url_path=url_path)
        if not os.path.exists(video_base_path):
            os.makedirs(video_base_path)

    def record_video(self, seconds_to_record):
        cap = cv2.VideoCapture(self.url_address)

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        fourcc = cv2.VideoWriter_fourcc(*'h264')
        video_name = datetime.now().strftime("%d-%B-%Y %Hh%Mm%Ss") + video_extension
        full_video_path = os.path.join(video_base_path, video_name)
        writer = cv2.VideoWriter(full_video_path, fourcc, 20.0, (width, height))

        timeout = time.time() + seconds_to_record
        while True:
            ret, frame = cap.read()
            writer.write(frame)
            if time.time() > timeout:
                break

        cap.release()
        writer.release()

        return Video(full_video_path, width, height)

class Video:
    def __init__(self, path, width, height):
        self.path = path
        self.width = width
        self.height = height