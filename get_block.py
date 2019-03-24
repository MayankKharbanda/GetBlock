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

    # Block found in Buffer Cache
    if buf_cache.in_hash_queue(block_num):          
        
        #assign pointer of the buffer
        block = buf_cache.assign_block(block_num)
        
        #scenario 5
        if BUFFER_STATUS['BUSY'] in block.get_status():
            # try again by returning and notifying the calling body.
            return None
        
        #scenario 1
        block.set_status('BUSY')
        buf_cache.free_list.remove(block)
        return block

    # Block NOT found in buffer Cache
    else:
        
        #scenario 4
        if buf_cache.free_list.is_empty():
            # try again by returning and notifying the calling body
            return None
       
        free_block = buf_cache.free_list.remove_from_head()     #pointer to the free block
        
        #scenario 3
        if BUFFER_STATUS['DELAYED_WRITE'] in free_block.get_status():
            #TODO handle asnchronous write
            free_block.remove_status('DELAYED_WRITE')
            buf_cache.free_list.add_to_head(free_block)
            return None
        
        #scenario 2
        if(free_block.block_number is not None):                 #if the buffer in free list was not present in any of the buffer list
            buf_cache.hash_queue_headers[free_block.block_number % Config.data("MAX_QUEUES")].remove(free_block)
            
        free_block.block_number = block_num
        buf_cache.hash_queue_headers[free_block.block_number % Config.data("MAX_QUEUES")].add(free_block)       
    
        free_block.set_status('BUSY') 
        return free_block
