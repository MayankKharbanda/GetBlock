'''
dummy made haphazardly
'''

import buffer_cache
import get_block
#import threading
#import subprocess
import time


#TODO signal from process to main

buf_cache = buffer_cache.BufferCache()

def read(blocknum, timestamp):
    print("in read")
    get_block.get_block(buf_cache, blocknum)
    
'''
def write():
    
    for i in range(1,20):
        subprocess.Popen("process"+i+".py", shell=True)
'''
'''
def process_creater():
    
    for i in range(1,20):
        subprocess.Popen("process"+i+".py", shell=True)
'''
#threading.Thread(target = process_creater).start()


def main():
    print("in main1")
    read(345,200)
    print("in main")
    time.sleep(0.02)
    #kernel.write(145,100)
    #time.sleep(0.01)
    #kernel.read(1235,200)
    #time.sleep(0.02)
if __name__=="__main__":
    main()
