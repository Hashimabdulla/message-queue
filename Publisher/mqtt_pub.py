from paho.mqtt.client import Client
import time
import json
# client = Client()
#
#
# def on_connect(client, userdata, flags, rc):
#     print("Connected")
#     client.publish("test", "Hello python")
#     print("Published")
#
#
# client.on_connect = on_connect
#
# client.connect("127.0.0.1")
# client.loop_forever()
from Publisher.base_publisher import BasePublisher


# time=time.time()

class MqttPublisher(BasePublisher):

    def __init__(self, *args, **kwargs):
        self.client = None
        self.message = None

    def connect(self, host="localhost", port=5000):
        self.client = Client()
        self.client.connect(host=host)
        print("Connected")

    def send_message(self, message, topic="test"):
        msg_size = len(message["message"])
        message["sentAt"] = time.time()
        message["size_in_BYTES"] = msg_size
        self.client.publish(topic=topic, payload=json.dumps(message))
        print("Published")

    def close(self):
        pass
