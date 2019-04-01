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
        "MAX_BLOCKS": 10,
        "MAX_BUFFERS": 4,
        "MAX_QUEUES": 2,
        "NUMBER_OF_PROCESSES": 5,
        "BUFFER_STATUS": {
            'BUSY': '0',
            'FREE': '1',
            'VALID': '2',
            'ACCESSING_DISK': '3',
            'PROCESS_WAITING': '4',
            'OLD':'5',
            'NOT_OLD':'6'
        },
        "FLAG": {
            'NONE':'0',
            'DELAYED_WRITE':'1',
            'BLOCK_BUSY':'2',
            'FREE_LIST_EMPTY':'3'
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

