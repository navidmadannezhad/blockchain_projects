from modules.main.socket_utils import Connection
from modules.transactions import Transaction
from modules.digital_signature import *

# - users
pu1, pr1 = generate_keys()
pu2, pr2 = generate_keys()
pu3, pr3 = generate_keys()

#  - transactions
tx1 = Transaction(pu1)
tx1.add_input(pu2, 3)
tx1.add_output(pu2, 2)
tx1.add_output(pu1, 1)
tx1.signTransactionWith(pr1)

tx2 = Transaction(pu2)
tx2.add_input(pu1, 1)
tx2.add_output(pu2, 1)
tx2.signTransactionWith(pr2)

# - sending to wallet
transactions = [tx1, tx2]
my_connection = Connection('localhost', 5500, 1024)
my_connection.send_data(transactions)