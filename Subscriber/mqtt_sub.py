from paho.mqtt.client import Client

client = Client()


def on_connect(client, userdata, flags, rc):
    print("Connected")
    client.on_message = on_message
    client.subscribe("test")


def on_message(client, userdata, message):
    print("Message received : {}".format(message.payload))


client.on_connect = on_connect

client.connect("127.0.0.1")

client.loop_forever()
