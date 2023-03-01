#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.log_util import logUtil
from utils.request_util import requestUtil


class Account(PreviewRequest):
    # 获取AccessToken
    def getAccessToken(self, data):
        requestUtil.openDocHook("获取AccessToken", self.dbUtil, ["rooms"])
        return self.post("api/account/get-access-token", data)