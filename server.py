import socket
import select

PORT = 5005
IP_ADDRESS = '127.0.0.1'

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket connected successfully')
except socket.error as err:
    print(f'we got an error: {err}')

s.bind((IP_ADDRESS, PORT))
s.listen(5)

readable_s, writable_s, exceptional_s = select.select([s], [], [s])

for s in readable_s:
    client, address = s.accept()
    client.send('fuck u!'.encode())
    client.close()
    break