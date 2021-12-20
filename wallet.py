import pickle
import threading
from config import private_key_path, dlt_path, miner_port, wallet_port

from modules.main.socket_utils import Connection
from modules.transactions import Transaction
from modules.digital_signature import *

def create_super_user():
    pu, pr = generate_keys()
    save_private_key = open(private_key_path, 'wb')
    pickle.dump(pr_to_pem(pr), save_private_key)

    
def load_superuser_keys():
    pr_file = open(private_key_path, 'rb')
    pem_pr = pickle.load(pr_file)
    pr = pem_to_pr_obj(pem_pr)
    pu = pr.public_key()
    return pr, pu


def ledger_is_present():
    return True if os.path.isfile(dlt_path) else False


def load_ledger():
    file = open(dlt_path, 'rb')
    ledger = pickle.load(file)
    return ledger

def find_balance(public_key, ledger):
    pass


# to send data
def wallet_server(data):
    wallet_server = Connection('localhost', wallet_port)
    wallet_server.send_data(data)

# to recieve data
def miner_server():
    miner_server = Connection('localhost', miner_port)
    miner_server.make_ready()
    for i in range(30):
        print(miner_server.recieve_data())


if __name__ == '__main__':

# 0 - loads itself keys from files
    create_super_user()
    pr1, pu1 = load_superuser_keys()

# create other users and transactions --------------
    pr2, pu2 = generate_keys()
    pr3, pu3 = generate_keys()

    tx1 = Transaction()
    tx1.add_input(pu2, 3)
    tx1.add_output(pu2, 3)
    tx1.signTransactionWith(pr1)

    tx2 = Transaction()
    tx2.add_input(pu1, 5)
    tx2.add_output(pu2, 4)
    tx2.add_output(pu1, 1)
    tx2.signTransactionWith(pr1)

    tx3 = Transaction()
    tx3.add_input(pu3, 10)
    tx3.add_output(pu2, 11)
    tx3.signTransactionWith(pr1)


# 1 - send tx to miner
# we send data from one port, and recieve data from another
    tx_list = [tx1, tx2, tx3]
    wallet_thread = threading.Thread(target=wallet_server, args=(tx_list))
    miner_thread = threading.Thread(target=miner_server)

    wallet_thread.start()
    miner_thread.start()

 

# 2 - recieve DLT 
    if ledger_is_present:
        print('Ledger is found')
        ledger = load_ledger()
    else:
        print('Ledger is not found')
        ledger = None

# 1.5 - recieve new balance of everyone

# 3 - save DLT