from config import Config

def get_block(buf_cache, block_num):
    '''
    Returns a Buffer

    input: pointer to buffer_cache
            block number
    output:
        pointer to the block in the buffer
    '''

    BUFFER_STATUS = Config.data("BUFFER_STATUS")

    #run till buffer is not returned
    while(True):      
       
        # Block found in Buffer Cache
        if buf_cache.in_hash_queue(block_num):          
            
            #assign pointer of the buffer
            block = buf_cache.assign_block(block_num)
            
            #scenario 5
            if BUFFER_STATUS['BUSY'] in block.get_status():
                #TODO sleep function on event - buffer becomes free
                continue
            
            #scenario 1
            block.set_status("busy")
            buf_cache.free_list.remove(block)
            return block
   
        # Block NOT found in buffer Cache
        else:
            
            #scenario 4
            if buf_cache.free_list.is_empty():
                #TODO sleep function on event - ANY buffer becomes free
                continue
           
            free_block = buf_cache.free_list.remove_from_head()     #pointer to the free block
            
            #scenario 3
            if(free_block.get_status == "delayed write"):
                #TODO handle asnchronous write
                continue
            
            #scenario 2
            if(free_block.block_number is not None):                 #if the buffer in free list was not present in any of the buffer list
                buf_cache.hash_queue_headers[free_block.block_number % Config.data("MAX_QUEUES")].remove(free_block)
                
            free_block.block_number = block_num
            buf_cache.hash_queue_headers[free_block.block_number % Config.data("MAX_QUEUES")].add(free_block)       
        
            return free_block
