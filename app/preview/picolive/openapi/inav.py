#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Inav(PreviewRequest):
    def getRoomInfo(self, data):
        requestUtil.openDocHook("获取房间信息", self.dbUtil, ["rooms"], False)
        return self.post("openapi/inav/room-info", data)