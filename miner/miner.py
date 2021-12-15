from modules.main.socket_utils import Connection
from config import max_tx_in_block
from modules.blockchain import Blockchain

my_connection = Connection('localhost', 5500, 1024)
my_connection.make_ready()

for i in range(2):
    tx_list = []
    blockchain1 = Blockchain()
    data = my_connection.recieve_data()
    # print(max_tx_in_block)
    for tx in data:
        tx_list.append(tx)
        if len(tx_list) is max_tx_in_block:
            blockchain1.createBlock(tx_list)
            print(blockchain1.blockList)
            # my_connection.terminate()

    # my_connection.terminate()