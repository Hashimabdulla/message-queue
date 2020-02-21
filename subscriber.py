from Subscriber import get_subscriber, subscribers

subscribers = get_subscriber(subscribers.ZEROMQ_SUBSCRIBER)
# subscribers = get_subscriber(subscribers.MQTT_SUBSCRIBER)
subscribers.connect()
subscribers.recv_message()