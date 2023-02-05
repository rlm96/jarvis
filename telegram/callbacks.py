import os
from telegram.ext import *

def watchman_callback(context: CallbackContext):
    if(context.job.context.door_sensor.has_change_status()):
        if(context.job.context.door_sensor.cached_status):
            try:
                context.bot.send_message(chat_id=context.job.context.allowed_chat, text="The door has been opened \U0001F6AA\U0001F6A8")
                video_name = context.job.context.rtsp_stream.record_video(10)
                context.bot.send_video(chat_id=context.job.context.allowed_chat, video=open(video_name, 'rb'))
                if(os.path.isfile(video_name)):
                    os.remove(video_name)
            except:
                if(os.path.isfile(video_name)):
                    os.remove(video_name)
        else:
            context.bot.send_message(chat_id=context.job.context.allowed_chat, text="The door has been closed \U0001F6AA\U00002705")
