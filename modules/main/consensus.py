import uuid
from cryptography.hazmat.primitives import hashes
from .. import config

class Hash_maker():
    block_data = None
    block_hash = None
    prevBlock_hash = None
    nonce = None

    def __init__(self, prevBlock_hash, block_data):
        self.block_data = block_data
        self.prevBlock_hash = prevBlock_hash

    def generate_hash(self):
        thisIsGenesisBlock = self.prevBlock_hash is None
        while True:
            hasher = hashes.Hash(hashes.SHA256())
            if thisIsGenesisBlock:
                hasher.update(bytes(str(self.block_data), 'utf-8'))
                hasher.update(bytes(str(self.generate_nonce()), 'utf-8'))
            else:
                hasher.update(bytes(str(self.block_data), 'utf-8'))
                hasher.update(bytes(str(self.prevBlock_hash), 'utf-8'))
                hasher.update(bytes(str(self.generate_nonce()), 'utf-8'))
            # turns /x into normal hex (when data is in byte form)
            self.block_hash = hasher.finalize().hex()
            print(self.block_hash)
            if self.hash_is_good():
                return self.block_hash


    def generate_nonce(self):
        return uuid.uuid4().hex

    def hash_is_good(self):
        must_zero_part = self.block_hash[0:1]
        for i in must_zero_part:
            try:
                # checks if i is letter or not. if not, continues to check if being zero
                i = int(i)
                if i is not 0:
                    return False
            except:
                return False
            return True
    


# Driver Code
if __name__ == "__main__":

    hasher = Hash_maker(prevBlock_hash="11", block_data="hi")
    myHash = hasher.generate_hash()
    print(myHash)
        

