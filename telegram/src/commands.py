from telegram.ext import *

async def health_command(update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.message.chat_id, text="Alive")
