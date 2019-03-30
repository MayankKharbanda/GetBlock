class HashQueue():
    
    
    def __init__(self, head=None, tail=None):
         
        self.head = head
        self.tail = tail
 
    
    def add(self, new_node):
        
        #adds a buffer into the buffer queue
        if self.head is None:
            self.head = self.tail = new_node
        
        else:
            new_node.prev_hash_queue = self.tail
            new_node.next_hash_queue = None
            self.tail.next_hash_queue = new_node
            self.tail = new_node
 
    
    def remove(self, current_node):

        #Removes buffer from a particular buffer list
        
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

    def show(self):
        
        #returns the state of a hash queue
        current_node = self.head
        
        print_string = ' | '

        while current_node is not None:
            
            s = (f'bno:{current_node.block_number} '
                 f'pid:{current_node.process_id}')
            print_string += s + ' | '
            
            current_node = current_node.next_hash_queue
        
        return print_string
