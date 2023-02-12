import os
from telegram.ext import *

async def watchman_callback(context: CallbackContext):
    if(context.job.data.door_sensor.has_change_status()):
        if(context.job.data.door_sensor.cached_status and context.job.data.sensor_true_on_open):
            try:
                await context.bot.send_message(chat_id=context.job.data.allowed_chat, text="The door has been opened \U0001F6AA\U0001F6A8")
                video = context.job.data.rtsp_stream.record_video(10)
                await context.bot.send_video(chat_id=context.job.data.allowed_chat, video=open(video.path, 'rb'), supports_streaming=True, width=video.width, height=video.height)
                if(os.path.isfile(video.path)):
                    os.remove(video.path)
            except:
                if(os.path.isfile(video.path)):
                    os.remove(video.path)
        else:
            await context.bot.send_message(chat_id=context.job.context.allowed_chat, text="The door has been closed \U0001F6AA\U00002705")
