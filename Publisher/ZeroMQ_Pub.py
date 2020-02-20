import zmq
import time

ctx = zmq.Context()
sock = ctx.socket(zmq.PUB)
sock.bind("tcp://127.0.0.1:1234")

print("Starting loop...")
while True:
    msg = "Hello world"
    sock.send_string(msg)
    print("Sent string: %s ..." % msg)
    time.sleep(1)
# msg = "Hello world "
# sock.send_string(msg)
# print("Sent string: %s ..." % msg)
sock.close()
ctx.term()
