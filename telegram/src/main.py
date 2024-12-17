import os
import sys
from telegram.ext import *
from dotenv import load_dotenv
import logging
import commands
import asyncio

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

application = Application.builder().token(os.getenv('BOT_API_KEY')).build()

allowed_chats = [int(x) for x in os.getenv('ALLOWED_CHATS_IDS').split(';')]

application.add_handler(CommandHandler('health', lambda update, context: commands.health_command(update, context, translator_singleton.translate(language, 'alive'))))

async def initialize_async():
    for allowed_chat in allowed_chats:
        await application.bot.send_message(chat_id=allowed_chat, 
            text=translator_singleton.translate(language, 'greet'))

if __name__ == '__main__':
    # run initialize_async() in the "background"
    # submit the coroutine to the event loop as a task before start bot polling
    asyncio.get_event_loop().create_task(initialize_async())
    application.run_polling()