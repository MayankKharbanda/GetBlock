import bufferHeader
import hashQueue
import freeQueue
from config import Config

class BufferCache:
    
    def __init__(self):
        '''
        Initializing the buffer cache with -
        + one free list
        + number of total buffers
        + total hash queues
        '''
        self.freeList = freeQueue.FreeQueue()    
        for x in range(config.data("MAX_BUFFERS")):                   
            self.freeList.add_to_tail(bufferHeader.BufferHeader())         
        
        self.hashQueueHeaders = []            
        for x in range(config.data("MAX_QUEUES")):                     
            self.hashQueueHeaders.append(hashQueue.HashQueue())
   

    def assign_block(self, blockNum):
        '''
        It returns the buffer pointer given the block number.
        This function is called only and only if, 
        a particular buffer exists in the buffer list
        '''
        
        #TODO correct name of hash_block
        
        hashBlock = self.hashQueueHeaders[blockNum % Config.data("MAX_QUEUES")].head
       

        while True:
            if hashBlock.blockNumber == blockNum:
                return hashBlock
            hashBlock = hashBlock.nextHashQueue
    
    
    def in_hash_queue(self, blockNum):
        '''
        It checks if the block is in hash queue or not
        '''
        
        hashBlock = self.hashQueueHeaders[blockNum % Config.data("MAX_QUEUES")].head
        
        while hashBlock is not None:
            if hashBlock.blockNumber == blockNum:
                return True
            hashBlock = hashBlock.nextHashQueue
        
        return False
