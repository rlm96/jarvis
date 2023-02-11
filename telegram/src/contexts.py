class BaseContext:
    def __init__(self) -> None:
        pass

class WatchmanContext(BaseContext):
    def __init__(self, allowed_chat, door_sensor, sensor_true_on_open, rtsp_stream):
        self.allowed_chat = allowed_chat
        self.door_sensor = door_sensor
        self.sensor_true_on_open = sensor_true_on_open
        self.rtsp_stream = rtsp_stream