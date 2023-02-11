import os
from telegram.ext import *
from dotenv import load_dotenv
import logging
import tuya
import rtsp
import commands
import callbacks
import contexts

logging.basicConfig(
    level = logging.INFO, format = "%(asctime)s %(message)s"
)
logger = logging.getLogger()

load_dotenv()

api_region = os.getenv('TUYA_API_REGION')
api_key = os.getenv('TUYA_API_KEY')
api_secret = os.getenv('TUYA_API_SECRET')
door_contact_sensor_device_id = os.getenv('TUYA_DOOR_CONTACT_SENSOR_DEVICE_ID')
tuya.configure_cloud(api_region, api_key, api_secret, door_contact_sensor_device_id)

door_sensor = tuya.ContactSensor(device_id=door_contact_sensor_device_id)

rtsp_stream = rtsp.Stream(os.getenv('CAMERA_IP'), os.getenv('RTSP_USER'), os.getenv('RTSP_PASSWORD'), os.getenv('RTSP_PATH'))

updater = Updater(os.getenv('BOT_API_KEY'), use_context=True)
dispatcher = updater.dispatcher

allowed_chat = int(os.getenv('ALLOWED_CHAT_ID'))

dispatcher.add_handler(CommandHandler('health', commands.health_command))

watchman_context = contexts.WatchmanContext(allowed_chat, door_sensor, os.getenv('CONTACT_SENSOR_TRUE_ON_OPEN'), rtsp_stream)
updater.job_queue.run_repeating(callbacks.watchman_callback, int(os.getenv('NOTIFICATION_RATE_S')), context=watchman_context)

updater.start_polling()
updater.idle()