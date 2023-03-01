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

    def exportPv(self, data):
        requestUtil.openDocHook("房间数据-观看次数", self.dbUtil, ["export"])
        return self.post("console/stat/export-pv", data)

    def exportApply(self, data):
        requestUtil.openDocHook("房间报名-下载", self.dbUtil, ["export"])
        return self.post("console/stat/export-apply", data)

    def exportList(self, data):
        requestUtil.openDocHook("房间报名-下载", self.dbUtil, ["export"])
        return self.post("console/export/list", data)

    def delete(self, data):
        requestUtil.openDocHook("下载中心-删除", self.dbUtil, ["export"])
        return self.post("console/export/delete", data)
