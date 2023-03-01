#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil

class Sign(PreviewRequest):
    def signFinish(self, data):
        requestUtil.openDocHook("签到-结束签到", self.dbUtil, ["room"])
        return self.post("v1/sign/sign-finish", data)