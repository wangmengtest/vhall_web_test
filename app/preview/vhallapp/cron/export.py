#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil
from utils.db_util import DBUtil


class Export(PreviewRequest):
    def exportIndex(self, data={}):
        requestUtil.openDocHook("内容下载 v2.0", self.dbUtil, ["record"])
        return self.post("cron/export/index", data)
