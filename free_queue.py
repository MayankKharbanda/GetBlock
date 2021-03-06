class FreeQueue():
    
    def __init__(self, head=None, tail=None):
        
        self.head = head
        self.tail = tail
   

    def add_to_tail(self, new_node):
        
        if self.head is None:
            self.head = self.tail = new_node
        
        else:
            new_node.prev_free_list = self.tail
            new_node.next_free_list = None
            self.tail.next_free_list = new_node
            self.tail = new_node
    
    
    def add_to_head(self, new_node):
        
        if self.head is None:
            self.head = self.tail = new_node
        
        else:
            new_node.next_free_list = self.head
            new_node.prev_free_list = None
            self.head.prev_free_list = new_node
            self.head = new_node
 
    
    def is_empty(self):
        return self.head == None
    
    
    def remove(self, current_node):
        
        #Removes buffer from free list
        
        #updating head/tail if needed
        if self.head == current_node:
            self.head = current_node.next_free_list
        if self.tail == current_node:
            self.tail = current_node.prev_free_list

        
        #updating the prev/next pointers after deletion
        if current_node.prev_free_list:
            current_node.prev_free_list.next_free_list = current_node.next_free_list
        if current_node.next_free_list:
            current_node.next_free_list.prev_free_list = current_node.prev_free_list
        
        
        #clearing the next and previous pointer of current node
        current_node.prev_free_list = None
        current_node.next_free_list = None
            
    
    def remove_from_head(self):
        
        #Removes buffer from head
        
        current_node = self.head
        self.tail = None if self.tail == current_node else self.tail
        self.head = current_node.next_free_list
        if(self.head):
            self.head.prev_free_list = None
        current_node.next_free_list = None
        return current_node
        
    def show(self):
        
        #returns the state of a hash queue
        
        current_node = self.head
        
        print_string = ' | ' 
        while current_node is not None:
            
            print_string += 'bno:' + str(current_node.block_number or -1)
            print_string += ' | '
            
            current_node = current_node.next_free_list
        
        return print_string
