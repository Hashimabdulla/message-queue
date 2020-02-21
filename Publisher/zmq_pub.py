# # import time.sleep
# import zmq
# context = zmq.Context()
# socket = context.socket(zmq.PUB)
# socket.bind('tcp://127.0.0.1:2000')
#
# # Allow clients to connect before sending
# # sleep(10)
# socket.send_pyobj({1:[1,2,3]})


from Publisher.base_publisher import BasePublisher
import zmq
import time


class ZeroMQPublisher(BasePublisher):
    def connect(self, host="127.0.0.1", port="1234"):
        self.ctx = zmq.Context()
        self.client = self.ctx.socket(zmq.PUB)
        self.client.bind("tcp://{}:{}".format(host, port))
        print("Starting loop...")

    def send_message(self, message="hello world"):
        while True:
            self.client.send_string(message)
            print("Sent string: %s ..." % message)
            time.sleep(1)

    def close(self):
        self.client.close()
        self.ctx.close()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = None

# send_msg("hello world")
# msg = "Hello world "
# sock.send_string(msg)
# print("Sent string: %s ..." % msg)
# zmq_object = ZeroMQPublisher()
# x = zmq_object.connect()
# y = zmq_object.send_message("hello world")
# zmq_object.close()