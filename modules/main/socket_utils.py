import socket
import pickle

PORT = 5005
IP_ADDRESS = '127.0.0.1'

def new_server_connection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP_ADDRESS, PORT))
    s.listen(5)
    return s


def recieve_data(socket):
    client, addr = socket.accept()
    data = b''
    while True:
        message = client.recv(1024)
        if not message:
            break
        data = data + message
    pickled_data = pickle.loads(data)
    return pickled_data


def send_data(ip_address, block):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, PORT))
    block_in_byte_format = pickle.dumps(block)
    s.send(block_in_byte_format)