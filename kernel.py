import threading
import time
import queue
import random

from buffer_cache import BufferCache
from get_block import get_block
from brelease import b_release
from request import Request
from request import ReleaseRequest
from request import Reply
from config import Config

BUFFER_STATUS = Config.data('BUFFER_STATUS')
FLAG_STATUS = Config.data("FLAG")

############# Daemon Threads Definations##############


'''
request_queue - contains requests for getblock algorithm
print_queue - contains print commands of details of the buffer
release_queue - contains requests for brelease algorithm

'''


request_queue = queue.Queue()
print_queue = queue.Queue()
release_queue = queue.Queue()



def requests_manager():
    
    #the function is used to handle getblock requests
    
    while True:
        
        req = request_queue.get()
        flag = FLAG_STATUS['NONE']
        
        #locking buffer cache to run get block
        with buf_cache_lock:
            block_free[req.block_number].clear()    #sleep other processes waiting for this block
            block, flag = get_block(buf_cache, req.block_number, req.process_id)

        if FLAG_STATUS['DELAYED_WRITE'] in flag:
            
            #sleep for asynchronous write to disk   
            delay_thread = threading.Thread(target=delay_func, args = (block,))
            delay_thread.start()
            req.return_queue.put(Reply(None, flag))
            
        elif FLAG_STATUS['BLOCK_BUSY'] in flag:   #didn't recieved the buffer in first go
            
            req.return_queue.put(Reply(None, flag))
        
        elif FLAG_STATUS['FREE_LIST_EMPTY'] in flag:   #didn't recieved the buffer in first go
            any_block_free.clear()      #sleep the process waiting for any block to free
            req.return_queue.put(Reply(None, flag))
            
        else:
            
            s =  (f'Process {req.process_id} '
                  f'acquired block {req.block_number} '
                  f'for {req.request_type}')
            print_queue.put(s)

            # if request was delayed write mark the status as data is valid 
            #and buffer is not old at the moment
            #checks are made if the buffer is already in the required hash queue
            if req.request_type is 'WRITE_DELAYED':
                if BUFFER_STATUS['VALID'] not in block.get_status():
                    block.set_status('VALID')
                if BUFFER_STATUS['NOT_OLD'] not in block.get_status():
                    block.set_status('NOT_OLD')

            print_queue.put(block)
            print_queue.put(buf_cache.show())

            # put locked buffer in the queue to be accessed by the process
            req.return_queue.put(Reply(block, flag))
        
        request_queue.task_done() #task for iteration is done -used while working with thread-queues



def delay_func(block1):
    
    #handles asynchronous write
    time_to_sleep = random.randint(1,3)
    time.sleep(time_to_sleep)
    
    #releasing the buffer after asynchronous write
    release_queue.put(ReleaseRequest(process_id="Kernel",
                                      block=block1))



def print_manager():
    
    #This function used to handle print requests of a buffer
    
    while True:
        data = print_queue.get()
        print(data)
        print_queue.task_done()



def release_manager():
    
    #This function is used to handle release requests of a buffer
    
    while True:
        req = release_queue.get()
        block_num = req.block.block_number
        
        with buf_cache_lock:    #locking the buffer cache
            b_release(buf_cache, req.block)
            
            #wake up the sleeping process
            block_free[block_num].set()
            any_block_free.set()
            
            
            s = (f'Process {req.process_id} '
                 f'releasing block {req.block.block_number}')
            print_queue.put(s)

            print_queue.put(buf_cache.show())
        
        release_queue.task_done()


################Daemon Threads initialization######################


requests_thread = threading.Thread(target=requests_manager)
requests_thread.daemon = True
requests_thread.start()
del requests_thread



print_thread = threading.Thread(target=print_manager)
print_thread.daemon = True
print_thread.start()
del print_thread



release_thread = threading.Thread(target=release_manager)
release_thread.daemon = True
release_thread.start()
del release_thread

###################### Processes Threads #############################

def worker(process_id):

    print_queue.put(f'Process {process_id} started.') 

    random_requests = random.randint(1,4)
    for ith_request in range(random_requests):
        #Requesting random block with access type of read, write and delayed write
        random_block = random.randint(0, Config.data('MAX_BLOCKS')-1)
        request_type = random.choice(Config.data('REQUEST_TYPE'))
        
        
        return_queue = queue.Queue()    #for exchange of block number from request_manager and the process
        return_val = Reply()
    
        
        s =  (f'Process {process_id} '
              f'requesting block {random_block} '
              f'for {request_type}')
        print_queue.put(s)

        while return_val.block is None:       #until buffer is not found

            request_queue.put(Request(process_id=process_id,
                                  block_number=random_block,
                                  request_type=request_type,
                                  return_queue=return_queue))
        
            return_val = return_queue.get()

            
            #sleep the process until buffer becomes free
            if FLAG_STATUS['BLOCK_BUSY'] in return_val.event:
                print_queue.put(f'Process {process_id} going to sleep because requested buffer is locked.')
                block_free[random_block].wait()
                print_queue.put(f'Process {process_id} wakes up.')
            elif FLAG_STATUS['FREE_LIST_EMPTY'] in return_val.event:
                print_queue.put(f'Process {process_id} going to sleep because free list is empty.')
                any_block_free.wait()
                print_queue.put(f'Process {process_id} wakes up.')
            
            return_queue.task_done()

        working_time = random.randint(0,3) 
        print_queue.put(f'Process {process_id} going to sleep for {working_time} seconds')
        time.sleep(working_time)     #sleep to represent process is working over the buffer
   
        s =  (f'Process {process_id} putting a release request '
              f'for block {random_block} '
              f'for {request_type}')
        print_queue.put(s)

        #requesting to release the buffer
        release_queue.put(ReleaseRequest(process_id=process_id,
                                      block=return_val.block))
    
    
  

######################## Cache Config ##########################

buf_cache = BufferCache()
buf_cache_lock = threading.Lock()
print_queue.put('Starting up!')
print_queue.put(buf_cache.show())

#########################Events##################################

any_block_free = threading.Event()
block_free = []
for i in range(Config.data("MAX_BLOCKS")):
    block_free.append(threading.Event())

#########################Process Threads Config##################

worker_threads = []


for i in range(Config.data("NUMBER_OF_PROCESSES")):
    process = threading.Thread(target=worker, args=[i])
    worker_threads.append(process)
    process.start()

########################Threads Termination######################
        
    
for t in worker_threads:
    t.join()

request_queue.join()
print_queue.join()
release_queue.join()
print_queue.put('Finishing')

##################################################################
