class SharedResource:
    
    def __init__(self, data, lock):
        self.lock = lock
        self.data = data


