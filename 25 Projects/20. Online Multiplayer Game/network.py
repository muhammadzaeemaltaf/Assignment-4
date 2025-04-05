import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.114"
        # self.server = "192.168.100.164"
        self.port = 5555
        self.sddr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.sddr)
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(f"Connection error: {e}")
            return None

    def send(self, data):
        try:
            self.client.send(str(data).encode() )
            response = pickle.loads(self.client.recv(2048))
            if not response:
                raise ConnectionError("No response received from the server.")
            return response
        except socket.error as e:
            print(f"Socket error: {e}")
            return None
