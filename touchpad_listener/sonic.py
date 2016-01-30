

import socket


def pack(s):
    s += '\0'
    if len(s) % 4:
        s += '\0' * (4 - (len(s) % 4))
    return s


class SonicPi(object):
    def __init__(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.connect(('localhost', 4557))

    def run(self, code):
        message = pack('/run-code') + pack(',ss') + pack('SonicPy') + pack(code)
        self._socket.send(message)

