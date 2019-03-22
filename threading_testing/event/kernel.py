from shared_resource import SharedResource
import threading
import random
from time import sleep
import logging

#####Logging#####

formatter = "%(asctime)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=formatter)
logger = logging.getLogger(__name__)

def logit(pid, res, status):
    res = f'resource {res}' if res is not None else " "*10
    logger.info(f'Process {pid} - {res} - {status}')

######Shared Resources######

SHARED_RESOURCES = 1

shared_resource_list = []
for i in range(SHARED_RESOURCES):
    shared_resource_list.append(SharedResource(i,threading.Event()))

#for res in shared_resource_list:
#    print(f'Shared Resource - {res.data} - {res.lock}')


######Threads######

def process(pid):
    logit(pid, None, "started")

    res = random.randint(0, SHARED_RESOURCES-1)
    logit(pid, res, "trying to lock")

    event = shared_resource_list[res].event
    while True:
        if event.is_set():
            event.clear()
            break
        event.wait()
    logit(pid, res, "locked")
    sleep(1)
    logit(pid, res, "releasing")
    event.set()

def kernel():
    logger.info('Kernel started')

######Main#####

kernel_thread = threading.Thread(target = kernel).start()
process1 = threading.Thread(target=process, args=[1]).start()
process2 = threading.Thread(target=process, args=[2]).start()
process3 = threading.Thread(target=process, args=[3]).start()


