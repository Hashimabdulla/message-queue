from paho.mqtt.client import Client

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


class MqttPublisher(BasePublisher):

    def connect(self, host="localhost", port=5000):
        self.client = Client()
        print("Connected")

    def send_message(self, topic="test",message="hello world"):
        self.client.publish(topic,message)
        print("Published")

    def close(self):
        pass

mqtt_object = MqttPublisher()
x = mqtt_object.connect()
y = mqtt_object.send_message("test","hello world")
# mqtt_object.close()