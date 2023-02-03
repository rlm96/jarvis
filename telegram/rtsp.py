import cv2
import time

base_address = "rtsp://{user}:{password}@{ip}/{path}"
video_name = 'output.mp4'

class Stream:
    def __init__(self, ip, user, password, path):
        self.url_address = base_address.format(ip=ip, user=user, password=password, path=path)

    def record_video(self, seconds_to_record):
        cap = cv2.VideoCapture(self.url_address)

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        writer = cv2.VideoWriter(video_name, fourcc, 20.0, (width,height))

        timeout = time.time() + seconds_to_record
        while True:
            ret, frame = cap.read()
            writer.write(frame)
            if time.time() > timeout:
                break

        cap.release()
        writer.release()

        return video_name