#!/usr/bin/env python
# encoding:utf8

import json
import require
import prettyprinter

"""
公共字符串JSON 类
"""


class StringJsonUtil(object):
    jsonObj = {}

    def __init__(self, string):
        self.jsonStr = string
        try:
            self.jsonObj = json.loads(string)
        except Exception as e:
            print(e)

    def get(self, key, default=None):
        if key in self.jsonObj:
            return self.jsonObj[key]
        else:
            return default

    def set(self, key, value):
        self.jsonObj[key] = value

    def string(self):
        return json.dumps(self.jsonObj, ensure_ascii=False)
