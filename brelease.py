from config import Config


def b_release(buf_cache, block):
    
    #releases the buffer from a process
    
    BUFFER_STATUS = Config.data('BUFFER_STATUS')
    
    if BUFFER_STATUS['VALID'] in block.get_status() and BUFFER_STATUS['OLD'] in block.get_status():
        #handles delayed write
        buf_cache.free_list.add_to_head(block)
        block.remove_status('OLD')
        block.remove_status('VALID')
    
    
    else:
        
        buf_cache.free_list.add_to_tail(block)
    
    block.process_id = -1
    block.remove_status('BUSY')
    block.lock.release()
    
