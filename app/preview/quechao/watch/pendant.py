#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Pendant(PreviewRequest):
    def clickPendant(self, data):
        requestUtil.openDocHook("挂件-点击挂架 v2.0", self.dbUtil, ["pendant"])
        return self.post("v2/pendant/click", data)

    def getLastPendant(self, data):
        requestUtil.openDocHook("挂件-获取最后一个推屏 v2.0", self.dbUtil, ["pendant"])
        return self.post("v2/pendant/get-last", data)
