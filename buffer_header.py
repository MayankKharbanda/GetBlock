

class Buffer_Header:
    
   
    
    def __init__(self, block_num=None, status=None, data=None,  next_hqueue=None, prev_hqueue=None, next_flist=None, prev_flist=None):
        self.block_num = block_num
        self.status = status
        self.data = data
        self.next_hqueue = next_hqueue
        self.prev_hqueue = prev_hqueue
        self.next_flist = next_flist
        self.prev_flist = prev_flist
        
    
    
    def get_block_num(self):
        return self.block_num
    
    
    
    def set_block_num(self, block_num):
        self.block_num = block_num
    
    
    
    def get_status(self):
        return self.status
    
    
    
    def set_status(self, status):
        self.status = status