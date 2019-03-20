

'''
buffer cache class

'''


import buffer_header
import hash_queue
import free_queue



class Buffer_Cache:

    

    
    def __init__(self):
        
        
        '''
            initializing the buffer cache in starting with 
                -number of total buffers
                -total hash queues
                -one free list
        '''
        
        
        #TODO buffer array deletion
        self.buffers = []                       #buffer array
        self.free_list = free_queue.Free_Queue()    #free list


        
        
        for x in range(2048):                   #number of buffers in the buffer cache --upto range
            self.buffers.append(buffer_header.Buffer_Header())      
            self.free_list.add_to_tail(self.buffers[x])         #adding all the buffers to the end of free list in starting
    
    
        
        self.hash_queue_headers = []            #array of hash queue headers
        
        for x in range(64):                     #number of hash-queues --upto range
            self.hash_queue_headers.append(hash_queue.Hash_Queue())

    
    
    
    
    def assign_block(self, block_num):
        
        
        
        '''
            it returns the buffer pointer given the block number
            this function is called only if, 
            a particular buffer exists in the buffer list
        '''
        
        
        #TODO correct name of hash_block
        
        hash_block = self.hash_queue_headers[block_num % 64].head
        
        while True:
            
            if hash_block.get_block_num() == block_num:
                return hash_block
            
            hash_block = hash_block.next_hqueue
    
    
    
    
    
    def in_hash_queue(self, block_num):
        
        '''
            it checks if the block is in hash queue or not
        '''
        
        
        hash_block = self.hash_queue_headers[block_num % 64].head
        
        
        while hash_block is not None:
            
            if hash_block.get_block_num() == block_num:
                return True
            
            hash_block = hash_block.next_hqueue
        
        
        return False