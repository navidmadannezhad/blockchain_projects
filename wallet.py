import os
import pickle
import threading
from config import private_key_path, dlt_path, miner_port, wallet_port

from modules.main.socket_utils import Connection
from modules.transactions import Transaction
from modules.digital_signature import *


def create_super_user():
    pr, pu = generate_keys()
    save_private_key = open(private_key_path, 'wb')
    pickle.dump(pr_to_pem(pr), save_private_key)

    
def load_superuser_keys():
    pr_file = open(private_key_path, 'rb')
    pem_pr = pickle.load(pr_file)
    pr = pem_to_pr_obj(pem_pr)
    pu = pr.public_key()
    # returns pr as object and pu and pem (to be able to pickle in socket connections)
    return pr, pu_to_pem(pu)


def ledger_is_present():
    return True if os.path.isfile(dlt_path) else False


def load_ledger():
    load_file = open(dlt_path, 'rb')
    ledger = []
    while True:
        try:
            transaction = pickle.load(load_file)
            ledger.append(transaction)
        except:
            # pickle items are finished
            load_file.close()
            break
        
    return ledger

def find_balance(public_key, ledger):
    user_balance = 0
    for transaction in ledger:
        for output in transaction.outputs:
            if output['to_address'] == public_key:
                user_balance = user_balance + output['amount']
    print(user_balance)


# to send data
def wallet_server(data):
    client_connection = Connection('localhost', wallet_port)
    client_connection.send_data(data)
    print('data is sent to miner --')

# to recieve data
def miner_server():
    server_connection = Connection('localhost', miner_port)
    server_connection.make_ready()
    print('wallet is listening now! --')
    for i in range(1):
        ledger = server_connection.recieve_data()
        # print(ledger)
        print('ledger is recieved from miner --')


if __name__ == '__main__':

# 0 - loads itself keys from files
    create_super_user()
    pr1, pu1 = load_superuser_keys()

# create other users and transactions --------------
    pr2, pu2 = generate_keys()
    pr3, pu3 = generate_keys()

    tx1 = Transaction(pu1)
    tx1.add_input(pu2, 5)
    tx1.add_output(pu2, 3)
    tx1.signTransactionWith(pr1)

    tx2 = Transaction(pu1)
    tx2.add_input(pu1, 5)
    tx2.add_output(pu2, 4)
    tx2.add_output(pu1, 1)
    tx2.signTransactionWith(pr1)

    tx3 = Transaction(pu1)
    tx3.add_input(pu3, 10)
    tx3.add_output(pu2, 11)
    tx3.signTransactionWith(pr1)


# 1 - send tx to miner
# we send data from one port, and recieve data from another
    tx_list = [tx1, tx2, tx3]
    wallet_thread = threading.Thread(target=wallet_server, args=(tx_list,))
    miner_thread = threading.Thread(target=miner_server)

    wallet_thread.start()
    miner_thread.start()

 

# 2 - recieve DLT 
    if ledger_is_present():
        print('Ledger is found')
        ledger = load_ledger()
        find_balance(pu2, ledger)
    else:
        print('Ledger is not found')
        ledger = None

# 1.5 - recieve new balance of everyone

# 3 - save DLT




    wallet_thread.join()
    miner_thread.join()