'''
Usage - say main module wants to access
the buffer size.

# main.py
from config import Config
Config.data("BUFFER_SIZE")
'''


class Config:
    __conf = {
        "BUFFER_SIZE": 1024,
        "BLOCK_SIZE": 1024,
        "MAX_BLOCKS": 2,
        "MAX_BUFFERS": 2,
        "MAX_QUEUES": 2,
        "BUFFER_STATUS": {
            'BUSY': '0',
            'FREE': '1',
            'VALID': '2',
            'DELAYED_WRITE': '3',
            'ACCESSING_DISK': '4',
            'PROCESS_WAITING': '5'
        },
        "REQUEST_TYPE": [
            "READ",
            "WRITE",
            "WRITE_DELAYED"
        ]
    }

    @staticmethod
    def data(name):
        return Config.__conf[name]

