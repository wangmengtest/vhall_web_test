#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil

class Code(PreviewRequest):
    def send(self, data):
        requestUtil.openDocHook("登录-短信验证", self.dbUtil, ["question"])
        return self.post("api/code/send", data)