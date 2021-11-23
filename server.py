import socket
import select
import pickle
from modules.main.socket_utils import *

#  --------------------------------------------------------------------
if __name__ == '__main__':
    socket = new_server_connection()
    data = recieve_data(socket)
    print(data)