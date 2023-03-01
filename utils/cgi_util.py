#!/usr/bin/env python
# encoding:utf8

import os
import require
from utils.log_util import logUtil
from utils.file_util import FileUtil

"""
Cgi类 单例
"""


class CgiUtil(object):
    def print(self, data):
        self.printHead()
        print(data)
        self.printFoot()

    def printLog(self):
        logUtil.logFile.close()
        logObj = FileUtil(require.logPath("/log.txt"), 'r')
        self.printHead()
        print(logObj.read())
        self.printFoot()

    def printJson(self):
        print("Content-type:text/json\n")

    def printHead(self, pre=True):
        print("Content-type:text/html\n")
        print('<html>')
        print('<head>')
        print('<title>网页测试</title>')
        print('<meta charset="utf-8" />')
        print('</head>')
        print('<body>')

        if pre:
            print('<pre>')

    def printFoot(self, pre=True):
        if pre:
            print('</pre>')

        print('</body>')
        print('</html>')




cgiUtil = CgiUtil()
