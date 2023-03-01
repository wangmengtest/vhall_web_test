#!/usr/bin/env python
# encoding:utf8

import os
import sys
import require
import prettyprinter
from utils.string_util import stringUtil

"""
输出HTML渲染 单例
"""


class HtmlRenderUtil(object):
    def __init__(self):
        self.htmlFile = open(require.logPath("/html.html"), 'w')

    def render(self, content, beauty=True, appendBr=True):
        try:
            if beauty:
                content = prettyprinter.pformat(content, indent=4, width=500, depth=10, ribbon_width=500)
                self.htmlFile.write(content)
            else:
                self.htmlFile.write(content)
            if appendBr:
                self.htmlFile.write("\r<br/><br/>\r\r")
            else:
                self.htmlFile.write("\r\r")
        except Exception as e:
            print(e)

    def renderStrJson(self, content):
        try:
            content = stringUtil.jsonStringFormat(content)
            self.htmlFile.write(content)
            self.htmlFile.write("\r<br/><br/>\r\r")
        except Exception as e:
            print(e)

    def renderJson(self, content, beauty=True, appendBr=True):
        try:
            content = stringUtil.jsonObjectFormat(content, beauty)
            self.htmlFile.write(content)

            if appendBr:
                self.htmlFile.write("\r<br/><br/>\r\r")
            else:
                self.htmlFile.write("\r\r")
        except Exception as e:
            print(e)

    def renderJsonLog(self, content):
        try:
            content = stringUtil.jsonObjectFormat(content)
            self.htmlFile.write(content)
            self.htmlFile.write("\r<br/><br/>\r\r")
        except Exception as e:
            print(e)



htmlRenderUtil = HtmlRenderUtil()
