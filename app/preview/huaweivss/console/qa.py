#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil

class Qa(PreviewRequest):
    def export(self, data):
        requestUtil.openDocHook("问答导出", self.dbUtil, ["rooms"])
        return self.post("console/qa/export", data)