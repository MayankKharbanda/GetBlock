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
        "MAX_BLOCKS": 100,
        "MAX_BUFFERS": 20,
        "MAX_QUEUES": 4
    }

    @staticmethod
    def data(name):
        return Config.__conf[name]

