#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Stat(PreviewRequest):
    def stat(self):
        requestUtil.openDocHook("内容统计 v2.0", self.dbUtil, ["record"])
        return self.post("cron/stat/stat", {})