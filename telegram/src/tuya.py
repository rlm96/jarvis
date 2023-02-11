import tinytuya

def configure_cloud(api_region, api_key, api_secret, api_device_id):
    global cloud 
    cloud = tinytuya.Cloud(api_region, api_key, api_secret, api_device_id)

class TuyaDevice:
    def __init__(self, device_id):
        if(cloud == None):
            raise Exception("Tuya Cloud not configured")
        self.device_id = device_id

class ContactSensor(TuyaDevice):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.cached_status = self.read_status()

    def read_status(self):
        status = cloud.getstatus(self.device_id)
        return status['result'][0]['value']

    def has_change_status(self):
        read_status = self.read_status()

        if(self.cached_status != read_status):
            self.cached_status = read_status
            return True
        
        return False