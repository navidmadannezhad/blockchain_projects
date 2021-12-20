import os

# ledger file information -----------------------------------
dlt_directory = './ledger/'
dlt_file = 'ledger'
dlt_format = 'dat'
dlt_path = os.path.join(dlt_directory, dlt_file)

# client keys file information -----------------------------------
def keys_directory():
    directory = './keys/'
    if not os.path.exists(directory):
        os.mkdir(directory)
    return directory
    
keys_directory = keys_directory()
private_key_file = 'private-key.dat'

private_key_path = os.path.join(keys_directory, private_key_file)

# mining information -----------------------------------
consensus_leading_zeros = 1

# connection data -----------------------------------
miner_port = 445
wallet_port = 135

# block information -----------------------------------
max_tx_in_block = 4
