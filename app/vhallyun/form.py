#!/usr/bin/env python
# encoding:utf8

import require
from app.vhallyun.vhallyun_request import VhallYunRequest
from utils.request_util import requestUtil


class Form(VhallYunRequest):
    def answerCreate(self, data):
        requestUtil.openDocHook("获取房间流状态", self.dbUtil)
        return self.post("api/v2/answer/create", data)
