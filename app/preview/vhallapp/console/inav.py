#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil

class Inav(PreviewRequest):
    def invite(self, data):
        requestUtil.openDocHook("邀请上麦", self.dbUtil, ["rooms"])
        return self.post("v2/inav/invite", data)

    def breakSpeak(self, data):
        requestUtil.openDocHook("预下麦", self.dbUtil, ["rooms"])
        return self.post("v2/inav/break-speak", data)

    def unableSpeak(self, data):
        requestUtil.openDocHook("无法上麦", self.dbUtil, ["rooms"])
        return self.post("v2/inav/unable-speak", data)

    def get(self, data):
        requestUtil.openDocHook("获取房间信息", self.dbUtil, ["rooms"])
        return self.post("api/inav/get", data)        