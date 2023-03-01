#!/usr/bin/env python
# encoding:utf8

import require
from app.vhallyun.vhallyun_request import VhallYunRequest
from utils.request_util import requestUtil


class Sdk(VhallYunRequest):
    def init(self, data):
        requestUtil.openDocHook("SDK房间初始化", self.dbUtil)
        return self.post("sdk/v2/init/start", data)

    def getAccessToken(self, data):
        requestUtil.openDocHook("SDK生成AccessToken", self.dbUtil)
        return self.post("api/v1/base/create-access-token", data)

