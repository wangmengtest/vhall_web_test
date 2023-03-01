#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Pendant(PreviewRequest):
    def pushScreen(self, data):
        requestUtil.openDocHook("挂件管理-推屏 v2.0", self.dbUtil, ["pendant"])
        return self.post("v2/pendant/push-screen", data)

    def getPushList(self, data):
        requestUtil.openDocHook("挂件管理-获取推屏列表 v2.0", self.dbUtil, ["pendant"])
        return self.post("v2/pendant/get-push-list", data)
