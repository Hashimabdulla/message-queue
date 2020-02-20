from Publisher.mqtt_pub import MqttPublisher
from Publisher.zmq_pub import ZeroMQPublisher
from Publisher import publishers

pubs = {
    publishers.ZEROMQ_PUBLISHER: ZeroMQPublisher,
    publishers.MQTT_PUBLISHER: MqttPublisher
}

def get_publisher(publisher_name):
    return pubs[publisher_name]()
