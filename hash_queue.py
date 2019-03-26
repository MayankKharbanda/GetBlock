class HashQueue():
    
    def __init__(self, head=None, tail=None):
        
        #initialize empty list
         
        self.head = head
        self.tail = tail
 
    
    def add(self, new_node):
        
        if self.head is None:
            self.head = self.tail = new_node
        
        else:
            new_node.prev_hash_queue = self.tail
            new_node.next_hash_queue = None
            self.tail.next_hash_queue = new_node
            self.tail = new_node
 
    
    def remove(self, current_node):

        #Removing buffer from a particular buffer list
        
        # updating head/tail if needed
        if self.head == current_node:
            self.head = current_node.next_hash_queue
        if self.tail == current_node:
            self.tail = current_node.prev_hash_queue
        
        # updating the prev/next pointers after deletion
        if current_node.prev_hash_queue:
            current_node.prev_hash_queue.next_hash_queue = current_node.next_hash_queue
        if current_node.next_hash_queue:
            current_node.next_hash_queue.prev_hash_queue = current_node.prev_hash_queue
        
        # clearing the next and previous pointer of current node
        current_node.prev_hash_queue = None
        current_node.next_hash_queue = None