class BaseContext:
    def __init__(self) -> None:
        pass

class WatchmanContext(BaseContext):
    def __init__(self, allowed_chat, door_sensor, rtsp_stream):
        self.allowed_chat = allowed_chat
        self.door_sensor = door_sensor
        self.rtsp_stream = rtsp_stream