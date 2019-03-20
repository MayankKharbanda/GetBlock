import get_block
import threading
import subprocess

#TODO signal from process to main

def read(self, blocknum, timestamp):
    get_block.get_block(blocknum)
    

def write():
    
    for i in range(1,20):
        subprocess.Popen("process"+i+".py", shell=True)


def process_creater():
    
    for i in range(1,20):
        subprocess.Popen("process"+i+".py", shell=True)


threading.Thread(target = process_creater).start()