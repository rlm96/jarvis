import os
from telegram.ext import *
from dotenv import load_dotenv
import logging
import commands
import callbacks
import callbacks.datamodels as datamodels

logging.basicConfig(
    level = logging.ERROR, format = "%(asctime)s %(message)s"
)
logger = logging.getLogger()

load_dotenv()

application = Application.builder().token(os.getenv('BOT_API_KEY')).build()

allowed_chat = int(os.getenv('ALLOWED_CHAT_ID'))

application.add_handler(CommandHandler('health', commands.health_command))

application.run_polling()