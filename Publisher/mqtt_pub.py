from paho.mqtt.client import Client

client = Client()


def on_connect(client, userdata, flags, rc):
    print("Connected")
    client.publish("test", "Hello world")
    print("Published")


client.on_connect = on_connect

client.connect("127.0.0.1")
client.loop_forever()
