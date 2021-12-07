import socket
import pickle

class Connection:
    s = None
    ip_address = None
    port = None
    buffer_size = None


    def __init__(self, ip_address, port, buffer_size=1024):
        self.ip_address = ip_address
        self.port = port
        self.buffer_size = buffer_size
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def send_data(self, data):
        self.s.connect((self.ip_address, self.port))
        data_in_byte_format = pickle.dumps(data)
        self.s.send(data_in_byte_format)


    def make_ready(self):
        self.s.bind((self.ip_address, self.port))
        self.s.listen()


    def recieve_data(self):
        client, addr = self.s.accept()
        data = b''
        while True:
            message = client.recv(1024)
            if not message:
                break
            data = data + message
        pickled_data = pickle.loads(data)
        return pickled_data


    def terminate(self):
        self.s.close()