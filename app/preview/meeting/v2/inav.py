#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil

class Inav(PreviewRequest):
    def userList(self, data):
        requestUtil.openDocHook("互动-用户列表", self.dbUtil, ["accounts"])
        return self.post("v2/inav/get-user-list", data)

    def getOnlineList(self, data):
        requestUtil.openDocHook("互动-成员列表", self.dbUtil, ["accounts"])
        return self.post("v2/inav/get-online-list", data)