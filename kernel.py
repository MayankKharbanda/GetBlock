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
release_queue = queue.Queue()

def requests_manager():
    while True:
        req = request_queue.get()
        with buf_cache_lock:
            block = get_block(buf_cache, req.block_number, req.process_id)

        if block is None:
            # the buffer was busy or was marked delayed write
            request_queue.put(req)
        else:
            print(f'Process {req.process_id} ',
                  f'acquired block {req.block_number}')

            # if request was delayed write mark the status as such
            if req.request_type is 'WRITE_DELAYED':
                block.set_status('DELAYED_WRITE')

            # put release request in the queue
            release_queue.put(Request(process_id=req.process_id,
                                      block_number=req.block_number,
                                      request_type='RELEASE', 
                                      block=block))
            print(block)

        request_queue.task_done()

def release_manager():
    while True:
        req = release_queue.get()
        time.sleep(2)
        print(f'Process {req.process_id} ',
              f'releasing block {req.block_number}')
        b_release(buf_cache, req.block)
        release_queue.task_done()
             

requests_thread = threading.Thread(target=requests_manager)
requests_thread.daemon = True
requests_thread.start()
del requests_thread

release_thread = threading.Thread(target=release_manager)
release_thread.daemon = True
release_thread.start()
del release_thread

########## Processes ##########

def worker(process_id):
    random_block = random.randint(0, Config.data('MAX_BLOCKS')-1)
    request_type = random.choice(Config.data('REQUEST_TYPE'))
    request_queue.put(Request(process_id=process_id,
                              block_number=random_block,
                              request_type=request_type))
  

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
release_queue.join()
print('Finishing')
