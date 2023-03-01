#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Diypage(PreviewRequest):
    def customTag(self, data):
        requestUtil.openDocHook("文档演示-归还权限", self.dbUtil, ["document"])
        return self.post("v2/diypage/custom-tag", data)
