import os
from telegram.ext import *
from dotenv import load_dotenv
import logging
import commands
import callbacks
import callbacks.datamodels as datamodels
import asyncio

logging.basicConfig(
    level = logging.ERROR, format = "%(asctime)s %(message)s"
)
logger = logging.getLogger()

load_dotenv()

application = Application.builder().token(os.getenv('BOT_API_KEY')).build()

allowed_chat = int(os.getenv('ALLOWED_CHAT_ID'))

application.add_handler(CommandHandler('health', commands.health_command))

async def initialize_async():
    await application.bot.send_message(chat_id=allowed_chat, 
        text="J.A.R.V.I.S. has been potentially rebooted. Check if everything is working as expected and devices (e.g., WiFi plugs and sensors) are in the required state (on/off)")

if __name__ == '__main__':
    # run initialize_async() in the "background"
    # submit the coroutine to the event loop as a task before start bot polling
    asyncio.get_event_loop().create_task(initialize_async())
    application.run_polling()