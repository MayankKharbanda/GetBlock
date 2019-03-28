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
        "MAX_BLOCKS": 50,
        "MAX_BUFFERS": 8,
        "MAX_QUEUES": 4,
        "NUMBER_OF_PROCESSES": 10,
        "BUFFER_STATUS": {
            'BUSY': '0',
            'FREE': '1',
            'VALID': '2',
            'DELAYED_WRITE': '3',
            'ACCESSING_DISK': '4',
            'PROCESS_WAITING': '5',
            'OLD':'6',
            'NOT_OLD':'7'
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

