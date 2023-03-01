#!/usr/bin/env python
# encoding:utf8

import require
from app.vps.vps_request import VpsRequest
from utils.request_util import requestUtil

class Qa(VpsRequest):
    def num(self, data):
        requestUtil.openDocHook("获取问答数量", self.dbUtil)
        return self.post("v1/question/question-nums", data)

    def lists(self, data):
        requestUtil.openDocHook("获取问答列表", self.dbUtil, None, False)
        return self.post("v3/question/lists", data)        