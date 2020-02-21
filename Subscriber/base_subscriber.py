import abc



class BaseSubscriber(abc.ABC):

    def __init__(self, *args, **kwargs):
        self.client = None
        self.message = None

    @abc.abstractmethod
    def connect(self, host="localhost", port=5000):
        pass

    @abc.abstractmethod
    def recv_message(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def close(self):
        pass