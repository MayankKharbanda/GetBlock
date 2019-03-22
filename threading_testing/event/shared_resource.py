import threading

class SharedResource:
    
    def __init__(self, data, event):
        self.data = data
        self.event = event
        self.event.set()


