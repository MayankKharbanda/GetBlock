#import buffer_header

class Free_Queue():
 
    
    
    def __init__(self, head=None, tail=None):
        
        self.head = head
        self.tail = tail
 
    
    
    
    
    
    def add_to_tail(self,  new_node):
        
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev_flist = self.tail
            new_node.next_flist = None
            self.tail.next_flist = new_node
            self.tail = new_node
    
    
    
    def is_Empty(self):
        return self.head == None
    
    
    
    
    def add_to_head(self,  new_node):
        
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next_flist = self.head
            new_node.prev_flist = None
            self.head.prev_flist = new_node
            self.head = new_node
 
    
    
    
    def remove(self, current_node):
        
        if self.head == current_node:
            self.head = current_node.next_flist
        if self.tail == current_node:
            self.tail = current_node.prev_flist

        if current_node.prev_flist:
            current_node.prev_flist.next_flist = current_node.next_flist
        if current_node.next_flist:
            current_node.next_flist.prev_flist = current_node.prev_flist
            
    
    
    def remove_from_head(self):
        
        node = self.head
        self.head = self.head.next_flist
        return node
        
     
    
    
    
    def show(self):
        
        print("Show list data:")
        
        current_node = self.head
        
        while current_node is not None:
            print(current_node.get_block_num())
            current_node = current_node.next_flist