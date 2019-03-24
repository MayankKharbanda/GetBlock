from config import Config

def get_block(buf_cache, block_num, process_id):
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
        block.lock.acquire()
        if BUFFER_STATUS['BUSY'] in block.get_status():
            # try again by returning and notifying the calling body.
            block.lock.release()
            return None
        
        #scenario 1
        block.lock.acquire()
        block.set_status('BUSY')
        block.process_id = process_id
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
            free_block.remove_status('BUSY')
            buf_cache.free_list.add_to_head(free_block)
            return None
        
        #scenario 2                 
        if(free_block.block_number is not None):
            #initially no buffer is in the hash queue
            hash_queue_no = free_block.block_number % Config.data("MAX_QUEUES")
            buf_cache.hash_queue_headers[hash_queue_no].remove(free_block)
            
        free_block.block_number = block_num
        hash_queue_no = free_block.block_number % Config.data("MAX_QUEUES")
        buf_cache.hash_queue_headers[hash_queue_no].add(free_block)       
        
        free_block.set_status('BUSY') 
        free_block.process_id = process_id
        free_block.lock.acquire()
        return free_block
