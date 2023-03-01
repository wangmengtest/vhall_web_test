#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Tools(PreviewRequest):
    def getEnv(self, data):
        requestUtil.openDocHook("获取env", self.dbUtil, ["record"])
        return self.post("cron/tools/get-env", data)