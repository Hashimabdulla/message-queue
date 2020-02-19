import zmq
context=zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.setsockopt_string(zmq.SUBSCRIBE, '')
subscriber.connect('tcp://127.0.0.1:1234')
subscriber.recv_multipart()
