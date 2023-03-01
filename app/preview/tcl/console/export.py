#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil
from utils.db_util import DBUtil


class Export(PreviewRequest):
    def exportIndex(self):
        requestUtil.openDocHook("内容下载 v2.0", self.dbUtil, ["record"])
        return self.post("cron/export/index", {})

    def exportLivePv(self, data):
        requestUtil.openDocHook("房间数据-直播观看次数", self.dbUtil, ["export"])
        return self.post("console/export/live-pv", data)

    def exportLiveUv(self, data):
        requestUtil.openDocHook("房间数据-直播观看次数", self.dbUtil, ["export"])
        return self.post("console/export/live-uv", data)

    def exportRecordPv(self, data):
        requestUtil.openDocHook("房间数据-回放观看次数", self.dbUtil, ["export"])
        return self.post("console/export/record-pv", data)

    def exportRecordUv(self, data):
        requestUtil.openDocHook("房间数据-回放观看次数", self.dbUtil, ["export"])
        return self.post("console/export/record-uv", data)