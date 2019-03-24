class Request:

    def __init__(self, 
                 process_id = None, 
                 block_number = None, 
                 request_type = None,
                 block = None):

        self.process_id = process_id
        self.block_number = block_number
        self.request_type = request_type
        self.block = block
