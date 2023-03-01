#!/usr/bin/env python
# encoding:utf8

import require
from app.vhallyun.vhallyun_request import VhallYunRequest
from utils.request_util import requestUtil


class Callback(VhallYunRequest):
    def streamChangeStatus(self, data):
        requestUtil.openDocHook("更改流状态", self.dbUtil, None, False)
        data["event"] = "lives/stream-change-status"
        return self.postJson("callback/lives/index", data, "signature")

    def liveIndex(self, data):
        requestUtil.openDocHook("直播回调", self.dbUtil, None, False)
        data["event"] = "lives/index"
        return self.postJson("callback/lives/index", data, "signature")
