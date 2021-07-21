""" به نام خداوند جان و خرد. کزین اندیشه برتر نگذرد """
from cryptography.hazmat.primitives import hashes


class Blockchain:
    blockCount = 0
    blockList = []

    def increamentBlockCount(self):
        self.blockCount = self.blockCount + 1


    def createBlock(self, data):
        if self.blockCount == 0:
            self.blockList.append(Block(data=data, prevHash=None, blockNumber=1))
        else:
            self.blockList.append(Block(data=data, prevHash=self.lastBlockHash(), blockNumber=self.blockCount+1))
        
        self.increamentBlockCount()


    def blockchainIsValid(self):
        pass

    def lastBlockHash(self):
        hash = self.blockList[self.blockCount-1].blockHash
        return hash

    



class Block:
    data = None
    blockNumber = None
    prevHash = None
    blockHash = None
    
    def __init__(self, data, prevHash, blockNumber):
        self.data = data
        self.prevHash = prevHash
        self.blockNumber = blockNumber
        self.computeHash(data, prevHash)

    def computeHash(self, data, prevHash):
        hasher = hashes.Hash(hashes.SHA256())
        thisIsGenesisBlock = prevHash is None
        if thisIsGenesisBlock:
            hasher.update(data)
        else:
            hasher.update(data)
            hasher.update(prevHash)
        self.blockHash = hasher.finalize()


    def __repr__(self):
        blockInformation = "Block number = {num}, block data = {data}, block hash = {hash}, previous block hash = {prevHash}".format(num=self.blockNumber, data=self.data, hash=self.blockHash, prevHash=self.prevHash)
        return blockInformation


    


myBlockchain = Blockchain()

message = b'This is the data to be stored'
myBlockchain.createBlock(message)

message2 = b'second message'
myBlockchain.createBlock(message2)

message3 = b'third message'
myBlockchain.createBlock(message3)

message4 = b'fourth message'
myBlockchain.createBlock(message4)

print(myBlockchain.blockList)
