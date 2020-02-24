from time import time

from paho.mqtt.client import Client
import json
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

    def __init__(self, *args, **kwargs):
        self.client = None
        self.message = None
        self.f=open("time_taken.txt","a+")
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
        print(message.payload)
        message = json.loads(message.payload)
        latency = time() - message["sentAt"]
        self.f.write("{}\n".format(latency))
        print("Message received : {} in {}".format(message, str(latency)))


    def close(self):
        pass
