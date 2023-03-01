#!/usr/bin/env python
# encoding:utf8

import require
import socket
from utils.config_util import configUtil

"""
TODO
Socket 类
"""


class SocketUtil(object):
    def __init__(self, url, port):
        self.openListen = True
        self.host = socket.gethostbyname(url)
        self.socketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socketObj.connect((self.host, port))

    def listen(self):
        with self.openListen:
            self.socketObj.listen()
            conn, addr = self.socketObj.accept()  # 等电话打进来
            data = conn.recv(1024)

            print(data)

            return data

    def send(self, msg):
        self.socketObj.send(msg)

    def close(self):
        self.openListen = False
        self.socketObj.close()

