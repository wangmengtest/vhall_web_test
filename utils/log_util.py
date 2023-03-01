#!/usr/bin/env python
# encoding:utf8

import os
import sys
import require
import logging
import prettyprinter
from utils.string_util import stringUtil

"""
公共日志类 单例
"""


class LogUtil(object):
    def __init__(self):
        logging.basicConfig(level=logging.ERROR,
                            format='asctime:        %(asctime)s \n'  # 时间
                                   'filename_line:  %(filename)s_[line:%(lineno)d] \n'  # 文件名_行号
                                   'level:          %(levelname)s \n'  # log级别
                                   'message:        %(message)s \n',  # log信息
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            stream=sys.stdout,
                            filemode='w')

        # JSON 类型日志，方便检索，调试(每次覆盖写)
        if os.path.exists(require.logPath("/log.json")):
            os.remove(require.logPath("/log.json"))
        self.jsonFile = open(require.logPath("/log.json"), 'w+')

        # 输出型日志，方便输出文档，错误信息等(每次覆盖写)
        if os.path.exists(require.logPath("/log.txt")):
            os.remove(require.logPath("/log.txt"))
        self.logFile = open(require.logPath("/log.txt"), 'w+')

    def info(self, content):
        try:
            content = "[INFO] " + str(content)
            self.logFile.write(content)
            self.logFile.write(2 * "\r")
        except Exception as e:
            print(e)

    def error(self, content):
        try:
            content = "[ERROR]" + str(content)
            self.logFile.write(content)
            self.logFile.write(2 * "\r")
        except Exception as e:
            print(e)

    def render(self, content, beauty=True, newLineNum=2):
        try:
            if beauty:
                content = prettyprinter.pformat(content, indent=4, width=500, depth=10, ribbon_width=500)
                self.logFile.write(content)
            else:
                self.logFile.write(content)
            self.logFile.write(newLineNum * "\r")
        except Exception as e:
            print(e)

    def renderStrJson(self, content):
        try:
            content = stringUtil.jsonStringFormat(content)
            self.jsonFile.write(content)
            self.jsonFile.write(2 * "\r")
        except Exception as e:
            print(e)

    def renderJson(self, content, beauty=True):
        try:
            content = stringUtil.jsonObjectFormat(content, beauty)
            self.logFile.write(content)
            self.logFile.write(2 * "\r")
        except Exception as e:
            print(e)

    def renderJsonLog(self, content):
        try:
            content = stringUtil.jsonObjectFormat(content)
            self.jsonFile.write(content)
            self.jsonFile.write(2 * "\r")
        except Exception as e:
            print(e)

    def renderStrJsonLog(self, content):
        try:
            content = stringUtil.jsonStringFormat(content)
            self.jsonFile.write(content)
            self.jsonFile.write(2 * "\r")
        except Exception as e:
            print(e)

    def renderConsole(self, content):
        print(content)
        print(2 * "\r")


logUtil = LogUtil()
