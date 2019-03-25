from shared_resource import SharedResource
import threading
#import random
from time import sleep
import logging

#####Logging#####

formatter = "%(asctime)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=formatter)
logger = logging.getLogger(__name__)

def logit(pid, res, mode, status):
    res = f'resource {res}' if res is not None else " "*10
    mode = f'Mode:{mode}  ' if mode is not None else " "*10
    logger.info(f'Process {pid} - {res} - {mode} - Status:{status}')

######Shared Resources######

SHARED_RESOURCES = 3

shared_resource_list = []
for i in range(SHARED_RESOURCES):
    shared_resource_list.append(SharedResource(i,threading.Lock()))

#for res in shared_resource_list:
#    print(f'Shared Resource - {res.data} - {res.lock}')


######Threads######

def process(pid):
    
    try:
        
        proc = open("process"+str(pid)+".txt","r")
        
        #filehandling
    except IOError:
        
        print("Error: can\'t find process "+ pid +" or read data")
    
    
    else:
        logit(pid, None, None, "started")
        
        proc_commands = proc.readlines()
        for i in proc_commands:
            
            proc_command = i.split()
            
            '''
            here proc_command contains data of the form
            proc_command[0] contains mode of access -read/write
            proc_command[1] contains block number to access
            proc_command[2] contains time for access/sleep            
            '''
            
            #res = random.randint(0, SHARED_RESOURCES-1)
            
            logit(pid, proc_command[1], proc_command[0], "trying to lock")

            '''
            with construct automatically calls
            lock.acquire() when entering and
            lock.release() when exiting
            '''
            
            with shared_resource_list[int(proc_command[1])-1].lock:
                logit(pid, proc_command[1], proc_command[0], "locked")
                sleep(float(proc_command[2]))
                logit(pid, proc_command[1], proc_command[0], "releasing")
                
        logit(pid, None, None, "exiting")

def kernel():
    logger.info('Kernel started')

######Main#####

kernel_thread = threading.Thread(target = kernel).start()
process1 = threading.Thread(target=process, args=[1]).start()
process2 = threading.Thread(target=process, args=[2]).start()
process3 = threading.Thread(target=process, args=[3]).start()


