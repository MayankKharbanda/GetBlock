from config import Config

def b_release(buf_cache, block):
    
    BUFFER_STATUS = Config.data('BUFFER_STATUS')
    
    if BUFFER_STATUS['DELAYED_WRITE'] in block.get_status(): #and buffer.is_old()):
        buf_cache.free_list.add_to_head(block)
    else:
        buf_cache.free_list.add_to_tail(block)
    
    block.remove_status('BUSY')
    block.lock.release()
    
