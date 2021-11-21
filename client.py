import socket

PORT = 5005
IP_ADDRESS = '127.0.0.1'

s = socket.socket()
s.connect((IP_ADDRESS, PORT))

message = s.recv(1024).decode()
print(message)

s.close()
