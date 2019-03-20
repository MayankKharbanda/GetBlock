class FreeQueue():
    
    def __init__(self, head=None, tail=None):
        '''
        initialize empty list
        '''
        self.head = head
        self.tail = tail
   

    def add_to_tail(self, newNode):
        
        if self.head is None:
            self.head = self.tail = newNode
        
        else:
            newNode.prevFreeList = self.tail
            newNode.nextFreeList = None
            self.tail.nextFreeList = newNode
            self.tail = newNode
    
    
    def add_to_head(self, newNode):
        
        if self.head is None:
            self.head = self.tail = newNode
        
        else:
            newNode.nextFreeList = self.head
            newNode.prevFreeList = None
            self.head.prevFreeList = newNode
            self.head = newNode
 
    
    def is_empty(self):
        return self.head == None
    
    
    def remove(self, currentNode):
        '''
        Removing buffer from free list
        '''
        
        #updating head/tail if needed
        if self.head == currentNode:
            self.head = currentNode.nextFreeList
        if self.tail == currentNode:
            self.tail = currentNode.prevFreeList

        #updating the prev/next pointers after deletion
        if currentNode.prevFreeList:
            currentNode.prevFreeList.nextFreeList = currentNode.nextFreeList
        if currentNode.nextFreeList:
            currentNode.nextFreeList.prevFreeList = currentNode.prevFreeList
        
        #clearing the next and previous pointer of current node
        currentNode.prevFreeList = None
        currentNode.nextFreeList = None
            
    
    def remove_from_head(self):
        '''
        Removing buffer from head (for delayed write)
        '''
        
        node = self.head
        node.nextFreeList = None
        return node
        
     
    '''
    
    
    def show(self):
        
        print("Show list data:")
        
        current_node = self.head
        
        while current_node is not None:
            print(current_node.get_block_num())
            current_node = current_node.next_flist
    '''
