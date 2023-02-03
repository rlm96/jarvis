from telegram.ext import *

def health_command(update, context: CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id, text="Alive")
