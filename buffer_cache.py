import buffer_header
import hash_queue
import free_queue


class Buffer_Cache:

    
    def __init__(self):
        
        self.buffers = []
        self.free_list = free_queue.Free_Queue()


        for x in range(2048):
            self.buffers.append(buffer_header.Buffer_Header())
            self.free_list.add_to_tail(self.buffers[x])
    
    
        self.hash_queue_headers = []


        for x in range(64):
            self.hash_queue_headers.append(hash_queue.Hash_Queue())

    
    
    
    
    def get_block(self, block_num):
        
        hash_block = self.hash_queue_headers[block_num % 64].head
        
        while True:
            
            if hash_block.get_block_num() == block_num:
                return hash_block
            hash_block = hash_block.next_hqueue
    
    
    
    
    
    def in_hash_queue(self, block_num):
        
        hash_block = self.hash_queue_headers[block_num % 64].head
        
        
        while hash_block is not None:
            
            if hash_block.get_block_num() == block_num:
                return True
            hash_block = hash_block.next_hqueue
        
        
        return False