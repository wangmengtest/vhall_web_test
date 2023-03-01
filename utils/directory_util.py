#!/usr/bin/env python
# encoding:utf8

import os
import require
import prettyprinter
import shutil
from utils.string_util import stringUtil

"""
目录工具
"""


class DirectoryUtil(object):
    def makeFileDir(self, file):
        fileDirList = file.split("/")
        fileDirList.pop()
        fileDir = "/".join(fileDirList)

        if not os.path.exists(fileDir):
            os.makedirs(fileDir)

    def makeDir(self, path):
        os.makedirs(fileDir)      

    def copy(self, path, targetPath):
        shutil.copy2(path, targetPath)    


directoryUtil = DirectoryUtil()