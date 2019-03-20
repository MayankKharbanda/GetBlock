import time
import kernel


kernel.read(12345,200)
time.sleep(0.02)
kernel.write(145,100)
time.sleep(0.01)
kernel.read(1235,200)
time.sleep(0.02)