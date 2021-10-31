# import config
# consensus code goes below here

# 0000000000000000000914460e6ecb0796c912e9370de609728436e926d553a5

# 0000000000000000000345ac45ace05338762b82b3aaa8d69c8eb78a2fb255f8

# 0000000000000000000036aa97dbe051f44cfbb5b44cea3b73a83b1975ede05b

# 19 ta sefr!

def block_hash(prevBlock_hash, block_data):
    hasher = hashes.Hash(hashes.SHA256())
    thisIsGenesisBlock = prevBlock_hash is None

    if thisIsGenesisBlock:
        hasher.update(bytes(str(data), 'utf-8'))
        hasher.update(bytes(str(nonce), 'utf-8'))
    else:
        hasher.update(bytes(str(data), 'utf-8'))
        hasher.update(bytes(str(prevBlockHash), 'utf-8'))
        hasher.update(bytes(str(nonce), 'utf-8'))

    return hasher.finalize()


def nonce(prevBlock_hash, block_data):
    
    desired_nonce = '111'
    return desired_nonce