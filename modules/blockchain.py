from .block import Block

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