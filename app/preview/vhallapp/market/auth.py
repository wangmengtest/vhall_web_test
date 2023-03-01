#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Auth(PreviewRequest):
    def marketLogin(self, data):
        requestUtil.openDocHook("控制台-云市场账号登录 v2.0", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("console/marketAuth/market-login", data)

    def marketConfig(self, data):
        requestUtil.openDocHook("控制台-云市场配置信息", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("console/marketAuth/isv-init", data)

