import uuid
from cryptography.hazmat.primitives import hashes

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

class Block_hash():
    block_data = None
    prevBlock_hash = None
    nonce = None

    def __init__(self, prevBlock_hash, block_data):
        self.block_data = block_data
        self.prevBlock_hash = prevBlock_hash

    def generate_hash(self):
        hasher = hashes.Hash(hashes.SHA256())
        thisIsGenesisBlock = self.prevBlock_hash is None

        if thisIsGenesisBlock:
            hasher.update(bytes(str(self.block_data), 'utf-8'))
            # hasher.update(bytes(str(nonce), 'utf-8'))
        else:
            hasher.update(bytes(str(self.block_data), 'utf-8'))
            hasher.update(bytes(str(self.prevBlock_hash), 'utf-8'))
            # hasher.update(bytes(str(nonce), 'utf-8'))
        # turns /x into normal hex (when data is in byte form)
        return hasher.finalize().hex()

    def generate_nonce(self):
        return uuid.uuid4().hex

    def hash_is_good():
        pass
    


# Driver Code
if __name__ == "__main__":

    hasher = Block_hash(prevBlock_hash="11", block_data="hi")
    myHash = hasher.generate_hash()
    print(myHash)
        

