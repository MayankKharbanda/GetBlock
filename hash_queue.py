


class Hash_Queue():
 
    
    
    def __init__(self, head=None, tail=None):
        
        self.head = head
        self.tail = tail
 
    
    
    def add(self,  new_node):
        
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev_hqueue = self.tail
            new_node.next_hqueue = None
            self.tail.next_hqueue = new_node
            self.tail = new_node
 
    
    
    
    def remove(self, current_node):
        
        if self.head == current_node:
            self.head = current_node.next_hqueue
        if self.tail == current_node:
            self.tail = current_node.prev_hqueue

        if current_node.prev_hqueue:
            current_node.prev_hqueue.next_hqueue = current_node.next_hqueue
        if current_node.next_hqueue:
            current_node.next_hqueue.prev_hqueue = current_node.prev_hqueue
            

        
    
    
    def show(self):
        
        print("Show list data:")
        
        current_node = self.head
        
        while current_node is not None:
            print(current_node.get_block_num())
            current_node = current_node.next_hqueue