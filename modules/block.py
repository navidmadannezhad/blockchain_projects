from cryptography.hazmat.primitives import hashes
from .blockFileCreator import BlockFileCreator

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
        print(self.data[0].inputs);
        createBlockFile = BlockFileCreator(content=self.data[0], suffix=self.blockNumber)

    def computeHash(self, data, prevBlockHash):
        hasher = hashes.Hash(hashes.SHA256())
        thisIsGenesisBlock = prevBlockHash is None
        if thisIsGenesisBlock:
            hasher.update(bytes(str(data), 'utf-8'))
        else:
            hasher.update(bytes(str(data), 'utf-8'))
            hasher.update(bytes(str(prevBlockHash), 'utf-8'))
        return hasher.finalize()

    def __repr__(self):
        return "Block Number: {}\n".format(self.blockNumber)+" data: {}\n".format(self.data)+" previous block hash: {}\n".format(self.prevBlockHash)+" block hash: {}\n".format(self.blockHash)+'\n\n'