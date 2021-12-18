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
            # validating the transactions
            transactions = block.data
            for transaction in transactions:
                if not transaction.is_valid():
                    print(f'block number {self.blockList.index(block)} is not valid\nCause of invalidity: invalid Transaction found')
                    return False

            # validating the block
            if self.blockList.index(block) is not len(self.blockList) - 1:
                newTestBlockHash = block.computeHash(data=block.data, prevBlockHash=block.prevBlockHash)

                if newTestBlockHash != self.blockList[self.blockList.index(block)+1].prevBlockHash:
                    print(f'block number {self.blockList.index(block)} is not valid\nCause of invalidity: invalid Block Hash')
                    return False
            
            return True


    def lastBlock(self):
        lastBlock = self.blockList[len(self.blockList) - 1]
        return lastBlock

    def __repr__(self):
        return str(self.blockList)