from Subscriber.mqtt_sub import MqttSubscriber
from Subscriber.zmq_sub import ZeroMQSubscriber
from Subscriber import subscribers

subs = {
    subscribers.ZEROMQ_SUBSCRIBER: ZeroMQSubscriber,
    subscribers.MQTT_SUBSCRIBER: MqttSubscriber
}

def get_subscriber(subscriber_name):
    return subs[subscriber_name]()