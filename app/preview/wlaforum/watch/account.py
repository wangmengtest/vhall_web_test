#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Account(PreviewRequest):
    def loginByMasterToken(self, data):
        requestUtil.openDocHook("通过主站token登录", self.dbUtil, ["rooms"], False)
        return self.post("v4/account/api/auth/login-by-master-station-token", data)

    def createMasterToken(self, data):
        requestUtil.openDocHook("生成主站token", self.dbUtil, ["rooms"], False)
        return self.post("v4/account/api/auth/generate-jwt-token", data)