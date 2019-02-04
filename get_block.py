import buffer_cache



def get_block(self, block_num):
    
    
    
    buf_cache = buffer_cache.Buffer_Cache()
    
    
    
    if buf_cache.in_hash_queue(block_num):
        
        block = buf_cache.get_block(block_num)
        if block.get_status == "busy":
            print("a")#continue
        
        block.set_status("busy")
        
        buf_cache.free_list.remove(block)
        
        return block
    
    
    
    else:
        
        if buf_cache.free_list.is_Empty():
            print("a")#continue
        
        free_block = buf_cache.free_list.remove_from_head()
        
        if(free_block.get_status == "delayed write"):
            print("write to disk")
        
        buf_cache.hash_queue_headers[(free_block.get_block_num())%64].remove(free_block)
        free_block.set_block_num(block_num)
        buf_cache.hash_queue_headers[(free_block.get_block_num())%64]
        
        
        return free_block