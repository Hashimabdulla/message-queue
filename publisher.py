from Publisher import get_publisher, publishers

publisher = get_publisher(publishers.ZEROMQ_PUBLISHER)

publisher.send_message()