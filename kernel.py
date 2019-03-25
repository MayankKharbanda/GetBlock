import threading
import time
import queue
import random

from buffer_cache import BufferCache
from get_block import get_block
from brelease import b_release
from request import Request
from config import Config

########## Daemon Threads ##########

request_queue = queue.Queue()
print_queue = queue.Queue()

def requests_manager():
    while True:
        req = request_queue.get()
        with buf_cache_lock:
            block = get_block(buf_cache, req.block_number, req.process_id)

        if block is None:
            req.return_queue.put(None)
        else:
            print(f'Process {req.process_id} ',
                  f'acquired block {req.block_number} ',
                  f'for {req.request_type}')

            # if request was delayed write mark the status as such
            if req.request_type is 'WRITE_DELAYED':
                block.set_status('DELAYED_WRITE')

            print_queue.put(block)
            
            # put locked buffer in the queue
            req.return_queue.put(block)
            
            #if req.request_type is 'WRITE_DELAYED':
            #    block.set_status('DELAYED_WRITE')

            #print(block)

        request_queue.task_done()


def print_manager():
    while True:
        data = print_queue.get()
        print(data)
        print_queue.task_done()


requests_thread = threading.Thread(target=requests_manager)
requests_thread.daemon = True
requests_thread.start()
del requests_thread

print_thread = threading.Thread(target=print_manager)
print_thread.daemon = True
print_thread.start()
del print_thread

########## Processes ##########

def worker(process_id):
    random_block = random.randint(0, Config.data('MAX_BLOCKS')-1)
    request_type = random.choice(Config.data('REQUEST_TYPE'))
    return_queue = queue.Queue()
    return_val = None
    
    while return_val is None:
        request_queue.put(Request(process_id=process_id,
                                  block_number=random_block,
                                  request_type=request_type,
                                  return_queue=return_queue))
        return_val = return_queue.get()
        return_queue.task_done()

    time.sleep(2)
    print(f'Process {process_id} ',
          f'releasing block {return_val.block_number}')
    b_release(buf_cache, return_val)
  

########## Cache Config ##########

buf_cache = BufferCache()
buf_cache_lock = threading.Lock()
print('Starting up!')

worker_threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=[i])
    worker_threads.append(t)
    t.start()
for t in worker_threads:
    t.join()

request_queue.join()
print_queue.join()
print('Finishing')
