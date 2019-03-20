from config import Config

def get_block(bufCache, blockNum):
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
        if bufCache.in_hash_queue(blockNum):          
            
            #assign pointer of the buffer
            block = bufCache.assign_block(blockNum)
            
            #scenario 5
            if BUFFER_STATUS['BUSY'] in block.get_status():
                #TODO sleep function on event - buffer becomes free
                continue
            
            #scenario 1
            block.set_status("busy")
            bufCache.freeList.remove(block)
            return block
   
        # Block NOT found in buffer Cache
        else:
            
            #scenario 4
            if bufCache.freeList.is_empty():
                #TODO sleep function on event - ANY buffer becomes free
                continue
            
            freeBlock = bufCache.freeList.remove_from_head()     #pointer to the free block
            
            #scenario 3
            if(freeBlock.get_status == "delayed write"):
                #TODO handle asnchronous write
                continue
            
            #scenario 2
            if(freeBlock.blockNumber is not None):                 #if the buffer in free list was not present in any of the buffer list
                bufCache.hash_queue_headers[freeBlock.blockNumber % Config.data("MAX_QUEUES")].remove(freeBlock)
                
            freeBlock.blockNumber = blockNum
            bufCache.hash_queue_headers[freeBlock.blockNumber % Config.data("MAX_QUEUES")].add(freeBlock)       
        
            return freeBlock
