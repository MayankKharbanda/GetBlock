class HashQueue():
    
    def __init__(self, head=None, tail=None):
        '''
        initialize empty list
        ''' 
        
        self.head = head
        self.tail = tail
 
    
    def add(self, newNode):
        
        if self.head is None:
            self.head = self.tail = newNode
        
        else:
            newNode.prevHashQueue = self.tail
            newNode.nextHashQueue = None
            self.tail.nextHashQueue = newNode
            self.tail = newNode
 
    
    def remove(self, currentNode):
        '''
        Removing buffer from a particular buffer list
        '''
        
        # updating head/tail if needed
        if self.head == currentNode:
            self.head = currentNode.nextHashQueue
        if self.tail == currentNode:
            self.tail = currentNode.prevHashQueue
        
        # updating the prev/next pointers after deletion
        if currentNode.prevHashQueue:
            currentNode.prevHashQueue.nextHashQueue = currentNode.nextHashQueue
        if currentNode.nextHashQueue:
            currentNode.nextHashQueue.prevHashQueue = currentNode.prevHashQueue
        
        # clearing the next and previous pointer of current node
        currentNode.prevHashQueue = None
        currentNode.nextHashQueue = None

        
'''    
    
    def show(self):
        
        print("Show list data:")
        
        current_node = self.head
        
        while current_node is not None:
            print(current_node.get_block_num())
            current_node = current_node.next_hqueue'''
