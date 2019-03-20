

'''

get block algorithm...

input: pointer to buffer_cache
        block number
output:
    pointer to the block in the buffer


'''



def get_block(buf_cache, block_num):
    
    while(True):                        #run till buffer is not returned
                                
        
        if buf_cache.in_hash_queue(block_num):          #buffer in hash queue
            
            block = buf_cache.assign_block(block_num)       #assign pointer of the buffer
            
            if block.get_status == "busy":          #scenario 5
                #TODO sleep function
                continue
            
            block.set_status("busy")                #scenario 1
            buf_cache.free_list.remove(block)
        
            return block
    
    
    
        else:                                   #buffer not in hash queue
            
            if buf_cache.free_list.is_Empty():      #scenario 4
                #TODO sleep function
                continue
            
            free_block = buf_cache.free_list.remove_from_head()     #pointer to the free block
        
            if(free_block.get_status == "delayed write"):           #scenario 3
                #TODO handle asnchronous write
                continue
            
            
            #scenario 2
            if(free_block.get_block_num() != None):                 #if the buffer in free list was not present in any of the buffer list
                buf_cache.hash_queue_headers[(free_block.get_block_num())%64].remove(free_block)
                
            free_block.set_block_num(block_num)
            buf_cache.hash_queue_headers[(free_block.get_block_num())%64].add(free_block)       
        
            return free_block