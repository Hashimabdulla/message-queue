# import zmq
# context = zmq.Context()
# socket = context.socket(zmq.SUB)
# # We can connect to several endpoints if we desire, and receive from all.
# socket.connect('tcp://127.0.0.1:2000')
#
# # We must declare the socket as of type SUBSCRIBER, and pass a prefix filter.
# # Here, the filter is the empty string, which means we receive all messages.
# # We may subscribe to several filters, thus receiving from all.
# socket.setsockopt_string(zmq.SUBSCRIBE, '')
#
# message = socket.recv_pyobj()
# print(message.get(1)[2])
from abc import ABC

from Subscriber.base_subscriber import BaseSubscriber

import zmq
import time
import json


class ZeroMQSubscriber(BaseSubscriber):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.message = None
        self.ctx = None
        self.f = open("time_taken_zmq.txt", "a+")

    def connect(self, host="127.0.0.1", port=1234):
        self.ctx = zmq.Context()
        self.client = self.ctx.socket(zmq.SUB)
        self.client.connect("tcp://{}:{}".format(host, port))
        self.client.subscribe("")  # Subscribe to all topics
        print("Starting to receive the message")

    def recv_message(self):
        while True:
            message = self.client.recv_string()
            message = json.loads(message)
            latency = time.time() - message["sendAt"]
            msg_size = len(message["message"].encode('utf-8'))
            print("Received string: {} size is {} and it took {} seconds".format(message, msg_size, latency))
            self.f.write("{} : {}\n".format(msg_size,latency))

    def close(self):
        self.client.close()
        self.ctx.close()

# zmq_object = ZeroMQSubscriber()
# x = zmq_object.connect()
# y = zmq_object.recv_message("message")
# zmq_object.close()
