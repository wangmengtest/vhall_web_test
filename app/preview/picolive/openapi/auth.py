#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Auth(PreviewRequest):
    def getVhallToken(self, data):
        requestUtil.openDocHook("控制台-获取临时授权 v2.0", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("openapi/auth/get-vhall-token", data)

