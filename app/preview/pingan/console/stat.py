#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.config_util import configUtil
from utils.request_util import requestUtil
from utils.db_util import DBUtil


class Stat(PreviewRequest):
    def statLive(self, data):
        requestUtil.openDocHook("房间管理-统计-房间 v2.0", self.dbUtil, ["rooms"])
        return self.post("console/stat/live", data)

    def getAttends(self, data):
        requestUtil.openDocHook("房间管理-直播观看详情 v2.0", self.dbUtil, ["rooms"])
        return self.post("console/stat/getAttends", data)

    def getRealAttends(self, data):
        requestUtil.openDocHook("房间管理-实时观看详情 v2.0", self.dbUtil, ["accounts", "room_real_attends"])
        return self.post("console/stat/get-real-time-attends", data)

    def exportRealAttends(self, data):
        requestUtil.openDocHook("房间管理-导出实时观看详情 v2.0", self.dbUtil, ["accounts", "room_real_attends"])
        return self.post("console/stat/export-real-time-attends", data)
