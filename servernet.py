import json
import threading
import zmq

TOPIC = "WEST"
CONTEXT = zmq.Context()

SENDER_ADDR = "tcp://52.6.204.171:1978"
SENDER_SOCKET = None

RECEIVER_ADDR = "tcp://52.6.204.171:1979"
RECEIVER_THREAD = None
RECEIVED_DATA = []


def send(msg):
    global SENDER_SOCKET
    if SENDER_SOCKET is None:
        print("creating sender socket")
        SENDER_SOCKET = CONTEXT.socket(zmq.PUB)
        SENDER_SOCKET.connect(SENDER_ADDR)

    SENDER_SOCKET.send((TOPIC + json.dumps(msg)).encode())


def receive():
    global RECEIVER_THREAD
    if RECEIVER_THREAD is None:
        def worker():
            try:
                print("creating receiver socket")
                soc = CONTEXT.socket(zmq.SUB)
                soc.setsockopt(zmq.SUBSCRIBE, TOPIC.encode())
                soc.connect(RECEIVER_ADDR)

                while True:
                    msg = soc.recv().decode()
                    assert msg.startswith(TOPIC)
                    msg = json.loads(msg[len(TOPIC):])
                    RECEIVED_DATA.append(msg)

            finally:
                print("closing receiver socket")
                soc.close()

        RECEIVER_THREAD = threading.Thread(target=worker, daemon=True)
        RECEIVER_THREAD.start()

    global RECEIVED_DATA
    data = RECEIVED_DATA
    RECEIVED_DATA = []
    return data


def test():
    import sys
    import time
    msg = sys.argv[-1]

    num = 0
    while True:
        num += 1
        send(msg)
        time.sleep(0.1)
        print("received", num, receive())
        time.sleep(0.9)


if __name__ == '__main__':
    test()
