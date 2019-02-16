import get_block
import threading

def process_creater():
    for i in range(1,20):
        #TODO call processes
        print(i)


threading.Thread(target = process_creater).start()