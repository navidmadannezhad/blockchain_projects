from modules.blockchain import Blockchain
from modules.transactions import Transaction
from modules.digital_signature import generate_keys


# navid test ------------------------------

# we have 3 users
pu1, pv1 = generate_keys()
pu2, pv2 = generate_keys()
pu3, pv3 = generate_keys()

# miner user
pu4, pv4 = generate_keys()

# tx1
tx1 = Transaction(pu1)
tx1.add_input(pu2, 8)
tx1.add_output(pu3, 8)
tx1.signTransactionWith(pv1)

# tx2
tx2 = Transaction(pu2)
tx2.add_input(pu1, 1)
tx2.add_output(pu3, 1)
tx2.signTransactionWith(pv2)

# tx3
tx3 = Transaction(pu3)
tx3.add_input(pu1, 2)
tx3.add_output(pu3, 2)
tx3.signTransactionWith(pv3)

# creating blockchain
hyperChain = Blockchain()

# miner base -------------------------------------------------------------------
tx4 = Transaction(pu4)
tx4.add_output(pu4, 25)
tx4.signTransactionWith(pv4)
# start mining
print(tx4)





