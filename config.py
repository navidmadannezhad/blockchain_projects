import os

dlt_directory = './ledger/'
dlt_file = 'block'
dlt_format = 'dat'
dlt_path = os.path.join(dlt_directory, dlt_file)

consensus_leading_zeros = 3

max_tx_in_block = 2