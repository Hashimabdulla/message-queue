from Publisher import get_publisher, publishers

publisher = get_publisher(publishers.ZEROMQ_PUBLISHER)
# publisher = get_publisher(publishers.MQTT_PUBLISHER)
publisher.connect()
# publisher.send_message(topic="test", message="hello")
publisher.send_message("hello zmq")