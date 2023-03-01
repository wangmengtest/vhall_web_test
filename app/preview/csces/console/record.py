#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Record(PreviewRequest):
    def recordList(self, data):
        requestUtil.openDocHook("内容-回放列表 v2.0", self.dbUtil, ["record"])
        return self.post("console/record/list", data)

    def relatedList(self, data):
        requestUtil.openDocHook("内容-精彩片段列表 v2.0", self.dbUtil, ["rooms"])
        return self.post("console/record/related-vod", data)

    def saveRelatedVod(self, data):
        requestUtil.openDocHook("内容-设置精彩片段 v2.0", self.dbUtil, ["record"])
        return self.post("console/record/save-related-vod", data)

    def download(self, data):
        requestUtil.openDocHook("内容-回放内容下载 v2.0", self.dbUtil, ["record"])
        return self.post("console/record/download", data)
