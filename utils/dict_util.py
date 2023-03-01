#!/usr/bin/env python
# encoding:utf8
import json
import prettyprinter
import require

"""
公共字符串类 列表
"""


class DictUtil(object):
    #  列表搜索
    def index(self, data, index):
        if index in data:
            return data[index]
        return -1

    def toJson(self, data):
        return json.dumps(data)    


dictUtil = DictUtil()
