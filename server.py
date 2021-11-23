import socket
import select
import pickle
from modules.socketUtils import *

#  --------------------------------------------------------------------
if __name__ == '__main__':
    socket = new_connection()
    data = recieve_data(socket)
    print(data)