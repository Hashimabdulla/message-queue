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
import json


class ZeroMQPublisher(BasePublisher):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = None


    def connect(self, host="127.0.0.1", port="1234"):
        self.ctx = zmq.Context()
        self.client = self.ctx.socket(zmq.PUB)
        self.client.bind("tcp://{}:{}".format(host, port))
        print("Sending the message")

    def send_message(self, message=dict()):
        msg_size = len(message["message"])

        t = time.time()
        print(message)
        message['sendAt'] = t
        message["size_in_BYTES"] = msg_size
        message = json.dumps(message)
        self.client.send_string(message)
        print("Sent string: %s " % message)
        # print("Message sent : {} in {}".format(message["message"], message["sendAt"]))
        time.sleep(0.1)

    def close(self):
        self.client.close()
        self.ctx.close()




# a=message["message"]="hello world"

# ZeroMQPublisher.send_message("""message":"Hello World""")
# msg = "Hello world "
# sock.send_string(msg)
# print("Sent string: %s ..." % msg)
# zmq_object = ZeroMQPublisher()
# x = zmq_object.connect()
# y = zmq_object.send_message("hello world")
# zmq_object.close()
