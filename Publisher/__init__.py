<<<<<<< HEAD
from .mqtt_pub import MqttPublisher
from .zmq_pub import ZeroMQPublisher
from . import publishers
=======
from Publisher.mqtt_pub import MqttPublisher
from Publisher.zmq_pub import ZeroMQPublisher
from Publisher import publishers
>>>>>>> 40421777d6543805c5607964f0b232ef858bff91

pubs = {
    publishers.ZEROMQ_PUBLISHER: ZeroMQPublisher,
    publishers.MQTT_PUBLISHER: MqttPublisher
}

def get_publisher(publisher_name):
    return pubs[publisher_name]()
