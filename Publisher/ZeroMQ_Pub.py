import zmq
context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.bind("tcp://127.0.0.1:1234")
publisher.send_multipart(["hello"])