import random
import time


async def delayed_write(buffer_cache, buffer):
    
    #sleep for asynchronous write to disk
    time_to_sleep = random.randint(1,3)
    time.sleep(time_to_sleep)
    
    #adding to free list after writing to the disk
    buffer_cache.free_list.add_to_head(buffer)
    buffer.remove_status('BUSY')
    
    buffer.lock.release()