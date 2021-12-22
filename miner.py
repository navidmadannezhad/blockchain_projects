import threading
import os
import pickle

from modules.main.socket_utils import Connection
from config import max_tx_in_block, miner_port, wallet_port, dlt_path, dlt_directory
from modules.blockchain import Blockchain
from modules.transactions import Transaction


validated_transactions = []
hyper_chain = Blockchain()
server_connection = Connection('localhost', wallet_port)
client_connection = Connection('localhost', miner_port)

def wallet_server():
    server_connection.make_ready()
    print('miner is listening! --')
    for i in range(30):
        print(client_connection)
        data = server_connection.recieve_data()
        print('data is recieved from wallet --')
        proccess_data(data)

                
def proccess_data(data):
    for item in data:
        if isinstance(item, Transaction):
            if item.is_valid():
                validated_transactions.append(item)
                save_to_ledger(item)
                ledger = load_ledger()
                miner_server(ledger)

    if hyper_chain.validateBlockchain():
        hyper_chain.createBlock(validated_transactions)
    else:
        print('blockchain is not valid')

    server_connection.terminate()


def save_to_ledger(data):
    if not os.path.exists(dlt_directory):
        os.mkdir(dlt_directory)
    save_file = open(dlt_path, 'ab')
    pickle.dump(data, save_file)


def load_ledger():
    load_file = open(dlt_path, 'rb')
    return pickle.load(load_file)
    
    
def miner_server(data):
    client_connection.send_data(data)
    print('data is sent to wallet --')








if __name__ == "__main__":
    
# 1 - recieve txs from wallet
# 2 - verify txs
    wallet_thread = threading.Thread(target=wallet_server)
    wallet_thread.start()

    wallet_thread.join()


# 3 - find the longest blockchain
#  -------------- still working on the same list index concept

# 4 - verify the blockchain


# 5 - put txs in block, find nonce


# 6 - set tx in ledger


# 7 - send the ledger to all wallets


