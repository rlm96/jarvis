import os
from telegram.ext import *
from dotenv import load_dotenv
import logging
import socket
import rtsp

logging.basicConfig(
    level = logging.ERROR, format = "%(asctime)s %(message)s"
)
logger = logging.getLogger()

load_dotenv()

udp_ip = ''
udp_port = os.getenv('UDP_PORT')

sensor_ip = os.getenv('CONTACT_SENSOR_IP')

rtsp_stream = rtsp.Stream(os.getenv('CAMERA_IP'), os.getenv('RTSP_USER'), os.getenv('RTSP_PASSWORD'), os.getenv('RTSP_PATH'))

application = Application.builder().token(os.getenv('BOT_API_KEY')).build()

allowed_chat = int(os.getenv('ALLOWED_CHAT_ID'))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udp_ip, udp_port))

async def new_method():
    try:
        await application.bot.send_message(chat_id=allowed_chat, text="The door has been opened \U0001F6AA\U0001F6A8")
        video = rtsp_stream.record_video(10)
        await application.bot.send_video(chat_id=allowed_chat, video=open(video.path, 'rb'), supports_streaming=True, width=video.width, height=video.height)
        if(os.path.isfile(video.path)):
            os.remove(video.path)
    except:
        if(os.path.isfile(video.path)):
            os.remove(video.path)

while True:
    data, addr = sock.recvfrom(1024)
    if addr[0] == sensor_ip:
        new_method()