#!/usr/bin/env python
# encoding:utf8

import os
import require
import prettyprinter
from utils.string_util import stringUtil
from utils.directory_util import directoryUtil

"""
文件工具
"""


class FileUtil(object):
    lines = []

    def __init__(self, file, mode="w+"):
        directoryUtil.makeFileDir(file)
        self.file = file
        self.handle = open(file, mode, encoding='utf-8')

    def printPath(self):
        currentPathList = self.file.split("toolkit")
        if len(currentPathList) == 2:
            print(currentPathList[0]+"toolkit"+currentPathList[1])         
            print("%s \n" % currentPathList[1][1:])
            
        else:
            print("%s \n \n" % self.file)

    def append(self, content):
        self.handle.write(content + "\n")

    def writeFirstLine(self, content):
        self.handle.seek(0, 0)
        self.write(content)

    def read(self):
        return self.handle.read()

    def write(self, content):
        self.handle.write(content)

    def readLines(self):
        if not self.lines:
            self.lines = self.handle.readlines()
        return self.lines

    def getMaxLineNum(self):
        return len(self.lines)

    def close(self):
        self.handle.close()