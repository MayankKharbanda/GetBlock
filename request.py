class Request:
    
    #This class is used to create objects for getblock requests 
    
    def __init__(self, 
                 process_id = None, 
                 block_number = None, 
                 request_type = None,
                 return_queue = None):

        self.process_id = process_id
        self.block_number = block_number
        self.request_type = request_type
        self.return_queue = return_queue


class ReleaseRequest:

    #This class is used to create objects for buffer release requests
    
    def __init__(self, 
                 process_id = None,
                 block = None):

        self.process_id = process_id
        self.block = block

class Reply:
    
    #This class is used to create objects for reply from request manager
    
    def __init__(self,
                 block = None,
                 event = 0):
        self.block = block
        self.event = event