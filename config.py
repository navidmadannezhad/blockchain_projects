import os

# ledger file information -----------------------------------
dlt_directory = './miner/'
dlt_file = 'ledger'
dlt_format = 'dat'
dlt_path = os.path.join(dlt_directory, dlt_file)

<<<<<<< HEAD
# client keys file information -----------------------------------
keys_directory = './wallet/'
private_key_file = 'private-key'
public_key_file = 'public-key'
keys_format = 'dat'

private_key_path = os.path.join(keys_directory, private_key_file)
public_key_path = os.path.join(keys_directory, public_key_file)

# mining information -----------------------------------
consensus_leading_zeros = 1

# connection data -----------------------------------
miner_port = 445
wallet_port = 135
=======
consensus_leading_zeros = 3

max_tx_in_block = 2
>>>>>>> 2f41aa7139664aadd3a18a347494ab16beacc7bb
