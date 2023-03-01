#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Room(PreviewRequest):
    def getStreamAddress(self, data):
        requestUtil.openDocHook("获取推流地址 v2.0", self.dbUtil, ["rooms"])
        return self.post("admin/room/get-stream-address", data)

    def setDefaultRecord(self, data):
        requestUtil.openDocHook("内容-设置默认回放 v2.0", self.dbUtil, ["rooms"])
        return self.post("admin/room/set-default-record", data)
