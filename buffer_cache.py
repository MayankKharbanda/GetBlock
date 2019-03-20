import buffer_header
import hash_queue
import free_queue
from config import Config

class BufferCache:
    
    def __init__(self):
        '''
        Initializing the buffer cache with -
        + one free list
        + number of total buffers
        + total hash queues
        '''
        self.free_list = free_queue.FreeQueue()    
        for x in range(Config.data("MAX_BUFFERS")):                   
            self.free_list.add_to_tail(buffer_header.BufferHeader())         
        
        self.hash_queue_headers = []            
        for x in range(Config.data("MAX_QUEUES")):                     
            self.hash_queue_headers.append(hash_queue.HashQueue())
   

    def assign_block(self, block_num):
        '''
        It returns the buffer pointer given the block number.
        This function is called only and only if, 
        a particular buffer exists in the buffer list
        '''
        
        #TODO correct name of hash_block
        
        hash_block = self.hash_queue_headers[block_num % Config.data("MAX_QUEUES")].head
       

        while True:
            if hash_block.block_number == block_num:
                return hash_block
            hash_block = hash_block.next_hash_queue
    
    
    def in_hash_queue(self, block_num):
        '''
        It checks if the block is in hash queue or not
        '''
        
        hash_block = self.hash_queue_headers[block_num % Config.data("MAX_QUEUES")].head
        
        while hash_block is not None:
            if hash_block.block_number == block_num:
                return True
            hash_block = hash_block.next_hash_queue
        
        return False
