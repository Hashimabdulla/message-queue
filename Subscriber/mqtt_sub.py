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

    def connect(self, host="localhost", port=5000):
        print("Connected")
        self.client=Client()
        self.client.recv_message = self.recv_message
        self.client.subscribe("test")

    def recv_message(self, message):
        print("Message received : {}".format(message))


    def close(self):
        pass

mqtt_object = MqttSubscriber()
x = mqtt_object.connect("localhost",5000)
y = mqtt_object.recv_message("test")
# mqtt_object.close()