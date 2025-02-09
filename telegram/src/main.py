import os
from telegram.ext import *
from dotenv import load_dotenv
import logging
import commands
import asyncio

resources_file_path = 'resources/translations.json'

if __debug__:
    import sys
    sys.path.append(os.path.abspath("../jarvis/shared"))
    resources_file_path = 'telegram/src/resources/translations.json'

import translator

load_dotenv()

translator_singleton = translator.TranslatorSingleton(file_path=resources_file_path)
language = os.getenv('DEFAULT_LANGUAGE')

logging.basicConfig(
    level = logging.ERROR, format = "%(asctime)s %(message)s"
)
logger = logging.getLogger()

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