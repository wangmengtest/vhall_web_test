#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Pendant(PreviewRequest):
    def create(self, data, path):
        requestUtil.openDocHook("挂件管理-添加挂件 v2.0", self.dbUtil, ["pendant"])
        return self.upload("console/pendant/create", 'pic', path, data)

    def update(self, data, path):
        requestUtil.openDocHook("挂件管理-更新挂件 v2.0", self.dbUtil, ["pendant"])
        return self.upload("console/pendant/update", 'pic', path, data)

    def delete(self, data):
        requestUtil.openDocHook("挂件管理-删除挂件 v2.0", self.dbUtil, ["pendant"])
        return self.post("console/pendant/delete", data)

    def getList(self, data):
        requestUtil.openDocHook("挂件管理-挂件列表 v2.0", self.dbUtil, ["pendant"])
        return self.post("console/pendant/get-list", data)

    def pushScreen(self, data):
        requestUtil.openDocHook("挂件管理-推屏 v2.0", self.dbUtil, ["pendant"])
        return self.post("console/pendant/push-screen", data)

    def getStatList(self, data):
        requestUtil.openDocHook("挂件管理-获取统计数据 v2.0", self.dbUtil, ["pendant", "pendant_stats"])
        return self.post("console/pendant/get-stats-list", data)
