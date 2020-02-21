from paho.mqtt.client import Client

# client = Client()
#
#
# def on_connect(client, userdata, flags, rc):
#     print("Connected")
#     client.on_message = on_message
#     client.subscribe("test")
#
#
# def on_message(client, userdata, message):
#     print("Message received : {}".format(message.payload))
#
#
# client.on_connect = on_connect
#
# client.connect("127.0.0.1")
#
# client.loop_forever()

from Subscriber.base_subscriber import BaseSubscriber


class MqttSubscriber(BaseSubscriber):

    def connect(self, host="localhost", port=5000, topic="test"):
        print("Connected")
        self.client = Client()
        self.client.connect(host=host)
        self.client.on_message = self.recv_message
        self.client.on_subscribe = self.on_subscribe
        self.client.subscribe(topic)
        self.client.loop_forever()

    def on_subscribe(self, *args, **kwargs):
        print("Subscribed")

    def recv_message(self, client, userdata, message):
        print("Message received : {}".format(message.payload))

    def close(self):
        pass

    def __init__(self, *args, **kwargs):
        self.client = None
        self.message = None
