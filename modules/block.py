from .blockFileCreator import BlockFileCreator
from .main.consensus import Hash_maker

class Block:
    data = None
    blockNumber = None
    prevBlockHash = None
    blockHash = None

    def __init__(self, data, prevBlockHash, blockNumber):
        self.data = data
        self.prevBlockHash = prevBlockHash
        self.blockNumber = blockNumber
        self.blockHash = self.computeHash(data, prevBlockHash)

    def computeHash(self, data, prevBlockHash):
        thisIsGenesisBlock = prevBlockHash is None
        if thisIsGenesisBlock:
            hasher = Hash_maker(prevBlock_hash=None, block_data=data)
        else:
            hasher = Hash_maker(prevBlock_hash=self.prevBlockHash, block_data=data)
        return hasher.generate_hash()

    def __repr__(self):
        return "Block Number: {}\n".format(self.blockNumber)+" data: {}\n".format(self.data)+" previous block hash: {}\n".format(self.prevBlockHash)+" block hash: {}\n".format(self.blockHash)+'\n\n'

