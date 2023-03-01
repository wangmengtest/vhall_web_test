#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil

class Qa(PreviewRequest):
    def lists(self, data):
        requestUtil.openDocHook("观众-获取问答列表 V2.1.0", self.dbUtil, ["question"])
        return self.post("/v2/qa/lists", data)