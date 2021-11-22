from modules.block import Block
from modules.blockchain import Blockchain 
from modules.transactions import Transaction
from modules.digital_signature import *
import socket
import pickle

PORT = 5005

def send_block(ip_address, block):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, PORT))
    block_in_byte_format = pickle.dumps(block)
    s.send(block_in_byte_format)


if __name__ == '__main__':

    my_blockchain = Blockchain()

    pu1 , pr1 = generate_keys()
    pu2 , pr2 = generate_keys()
    pu3 , pr3 = generate_keys()

    # transaction of user 1 ---------------------------------------
    tx1 = Transaction(pu1)
    tx1.add_input(pu2, 5)
    tx1.add_input(pu3, 4)
    tx1.add_input(pu1, 1)

    tx1.add_output(pu2, 10)
    tx1.signTransactionWith(pr1)

    transactions = [tx1]
    valid_transactions = []

    for transaction in transactions:
        if transaction.is_valid():
            valid_transactions.append(transaction)

    my_blockchain.createBlock(valid_transactions)


    # transaction of user 2 -----------------------------------------
    tx2 = Transaction(pu2)
    tx2.add_input(pu3, 5)

    tx2.add_output(pu2, 5)
    tx2.signTransactionWith(pr2)

    transactions = [tx2]
    valid_transactions = []

    for transaction in transactions:
        if transaction.is_valid():
            valid_transactions.append(transaction)

    my_blockchain.createBlock(valid_transactions)

    blocks = my_blockchain.blockList
    send_block('localhost', blocks)  