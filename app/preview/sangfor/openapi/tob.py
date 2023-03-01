#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Tob(PreviewRequest):
    def verifyToken(self, data):
        requestUtil.openDocHook("华为tob验证token", self.dbUtil, [])
        return self.post("openapi/tob/verify-token", data)

    def apiVerifyToken(self, data, header):
        requestUtil.openDocHook("华为tob验证token", self.dbUtil, [])
        return self.postAppendHeader("api/tob/reflect-token", data, header)