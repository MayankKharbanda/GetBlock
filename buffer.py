class Buffer:
    
    def __init__(self,
                 blockNumber = None,
                 processId = None,
                 status = None,
                 data = None,
                 nextHashQueue = None,
                 prevHashQueue = None,
                 nextFreeList = None,
                 prevFreeList = None):
        
        self.blockNumber = blockNumber
        self.processId = processId
        self.status = status
        self.data = data
        self.nextHashQueue = nextHashQueue
        self.prevHashQueue = prevHashQueue
        self.nextFreeList = nextFreeList
        self.prevFreeList = prevFreeList

    def __str__(self):
        onFreeList = 'not on the free list' if nextFreeList is \
                        None else 'on the free list'
        hasdiskBlock = 'no' if self.blockNumber is None else self.blockNumber
        hasProcess = 'no' if self.processId is None else self.processId
                    
        return (f'This Buffer has the status as {self.status}. '
                f'It is {onFreeList} ' 
                f'and is assigned to {hasDiskBlock} disk block '
                f'which is procured by {hasProcess} process.')
        

