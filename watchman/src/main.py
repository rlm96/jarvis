import os
import sys
from telegram.ext import *
from dotenv import load_dotenv
import logging
import socket
import rtsp
import asyncio
import select

current_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.dirname(os.path.dirname(current_path))
shared_path = os.path.join(project_path, "shared")

if shared_path not in sys.path:
    sys.path.append(shared_path)

import translator

translator_singleton = translator.TranslatorSingleton(file_path='resources/translations.json')
language = os.getenv('DEFAULT_LANGUAGE')

logging.basicConfig(
    level = logging.ERROR, format = "%(asctime)s %(message)s"
)
logger = logging.getLogger()

load_dotenv()

udp_ip = ''
udp_port = int(os.getenv('UDP_PORT'))

sensor_ip = os.getenv('CONTACT_SENSOR_IP')

rtsp_stream = rtsp.Stream(os.getenv('CAMERA_IP'), os.getenv('RTSP_USER'), os.getenv('RTSP_PASSWORD'), os.getenv('RTSP_PATH'))

application = Application.builder().token(os.getenv('BOT_API_KEY')).build()

allowed_chats = [int(x) for x in os.getenv('ALLOWED_CHATS_IDS').split(';')]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udp_ip, udp_port))

def drain_socket():
    """Drain/empty any pending incoming data present in the socket"""
    input = [sock]
    while True:
        inputready, o, e = select.select(input,[],[], 0.0)
        if len(inputready)==0: break
        for s in inputready: s.recv(1024)

async def process_event_async():
    try:
        video = rtsp_stream.record_video(10)
        for allowed_chat in allowed_chats:
            await application.bot.send_message(chat_id=allowed_chat, text=translator_singleton.translate(language, 'event'))
            await application.bot.send_video(chat_id=allowed_chat, video=open(video.path, 'rb'), supports_streaming=True, width=video.width, height=video.height)
        if(os.path.isfile(video.path)):
            os.remove(video.path)
    except:
        if(os.path.isfile(video.path)):
            os.remove(video.path)

async def main():
    while True:
        data, addr = sock.recvfrom(1024)
        if addr[0] == sensor_ip:
            await process_event_async()
            drain_socket()

if __name__ == '__main__':
    asyncio.run(main())