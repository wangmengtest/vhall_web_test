#!/usr/bin/env python
# encoding:utf8

import require
from app.vhallyun.vhallyun_request import VhallYunRequest
from utils.request_util import requestUtil


class Question(VhallYunRequest):
    def getAnswerListAll(self, data):
        requestUtil.openDocHook("获取所有答卷", None)
        return self.post("api/v2/answer/list-all", data)
