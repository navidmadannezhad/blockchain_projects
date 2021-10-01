from modules.blockchain import Blockchain
from modules.transactions import Transaction
from modules.digital_signature import generate_keys

import pickle


# navid test ------------------------------

# we have 3 users
pu1, pv1 = generate_keys()
pu2, pv2 = generate_keys()
pu3, pv3 = generate_keys()

# user 1 creates a transaction
tx1 = Transaction(pu1)

# sends 8 coins to user 3, which has recieved from user 2 some time ago
tx1.add_input(pu2, 8)
tx1.add_output(pu3, 1)

# user 1 signs his/her own transaction
tx1.signTransactionWith(pv1)

# creating transaction 2
tx2 = Transaction(pu2)

tx2.add_input(pu1, 1)
tx2.add_output(pu3, 1)
tx2.signTransactionWith(pv2)



# creating blockchain
hyperChain = Blockchain()

data = [tx1, tx2]
validated_data = []

for tx in data:
    if tx.is_valid:
        validated_data.append(tx)
    
hyperChain.createBlock(validated_data)
print(hyperChain)



