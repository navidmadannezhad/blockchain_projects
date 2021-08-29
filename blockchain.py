from cryptography.hazmat.primitives import hashes


class Blockchain:
    blockList = []

    def createBlock(self, data):
        if len(self.blockList) is 0:
            block = Block(data=data, prevBlockHash=None, blockNumber=0)
            self.blockList.append(block)
        else:
            block = Block(data=data, prevBlockHash=self.lastBlock().blockHash, blockNumber=self.lastBlock().blockNumber + 1)
            self.blockList.append(block)

    def validateBlockchain(self):
        # need a good algorithm for validating
        for block in self.blockList:
            if self.blockList.index(block) is not len(self.blockList) - 1:
                newTestBlockHash = block.computeHash(data=block.data, prevBlockHash=block.prevBlockHash)

                if newTestBlockHash == self.blockList[self.blockList.index(block)+1].prevBlockHash:
                    print('block number {} is ok!'.format(self.blockList.index(block)))
                else:
                    print('block number {} is tampered'.format(self.blockList.index(block)))

    def lastBlock(self):
        lastBlock = self.blockList[len(self.blockList) - 1]
        return lastBlock

    def __repr__(self):
        return str(self.blockList)




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
        hasher = hashes.Hash(hashes.SHA256())
        thisIsGenesisBlock = prevBlockHash is None
        if thisIsGenesisBlock:
            hasher.update(bytes(str(data), 'utf-8'))
        else:
            hasher.update(bytes(str(data), 'utf-8'))
            hasher.update(bytes(str(prevBlockHash), 'utf-8'))
        return hasher.finalize()

    def __repr__(self):
        return "Block Number: {}\n".format(self.blockNumber)+" data: {}\n".format(self.data)+" previous block hash: {}\n".format(self.prevBlockHash)+" block hash: {}\n".format(self.blockHash)




myBlockchain = Blockchain()

myBlockchain.createBlock('hello')
myBlockchain.createBlock('this is the second')
myBlockchain.createBlock(123)

myBlockchain.validateBlockchain()