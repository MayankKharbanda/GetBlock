import random
import time
from brelease import b_release
import threading


def delayed_write(buffer_cache, buffer):
    
    buf_cache_lock = threading.Lock()
    #sleep for asynchronous write to disk
    
    time_to_sleep = random.randint(1,3)
    time.sleep(time_to_sleep)
    
    #releasing buffer after writing to the disk
    with buf_cache_lock:
        b_release(buffer_cache, buffer)