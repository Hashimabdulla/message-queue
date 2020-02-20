import abc


class BasePublisher(abc.ABC):

    def __init__(self, *args, **kwargs):
        self.client = None

    @abc.abstractmethod
    def connect(self, host="localhost", port=5000):
        pass

    @abc.abstractmethod
    def send_message(self, message="hello world"):
        pass

    @abc.abstractmethod
    def close(self):
        pass