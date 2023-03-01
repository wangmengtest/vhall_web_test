#!/usr/bin/env python
# encoding:utf8
import re
import os
import openpyxl
import require
import csv
from utils.log_util import logUtil
from utils.string_util import stringUtil

"""
公共CSV读文件处理 单例
"""


class CsvReadUtil(object):
    filePath = None
    encoding = 'utf-8'

    def __init__(self, filePath, encoding='utf-8'):
        self.filePath = filePath
        self.encoding = encoding

        if not os.path.exists(self.filePath):
            logUtil.renderConsole(self.filePath + " 文件不存在")
            exit(0)

    # 按给定的索引将表格映射进去
    def mapToIndex(self, startNum, indexArray):
        result = []
        index = 0

        with open(self.filePath, "r", encoding=self.encoding) as f:
            reader = csv.reader(f)
            for row in reader:
                index += 1
                loopData = {}
                if index >= startNum:
                    for key, value in enumerate(indexArray):
                        loopData[value] = re.compile('[\\x00-\\x08\\x0b-\\x0c\\x0e-\\x1f]').sub(' ', row[key])
                    result.append(loopData)

        return result


