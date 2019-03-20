class BufferHeader:
    
    def __init__(self,
                 block_number = None,
                 process_id = None,
                 status = None,
                 data = None,
                 next_hash_queue = None,
                 prev_hash_queue = None,
                 next_free_list = None,
                 prev_free_list = None):
        
        self.block_number = block_number
        self.process_id = process_id
        self.status = status
        self.data = data
        self.next_hash_queue = next_hash_queue
        self.prev_hash_queue = prev_hash_queue
        self.next_free_list = next_free_list
        self.prev_free_list = prev_free_list

    def __str__(self):
        on_free_list = 'not on the free list' if self.next_free_list is \
                        None else 'on the free list'
        has_disk_block = 'no' if self.block_number is None else self.block_number
        has_process = 'no' if self.process_id is None else self.process_id
                    
        return (f'This Buffer has the status as {self.status}. '
                f'It is {on_free_list} ' 
                f'and is assigned to {has_disk_block} disk block '
                f'which is procured by {has_process} process.')
        
    
    def get_status(self):
        return self.status


    def set_status(self, status):
        self.status += status
