#!/usr/bin/env python
# encoding:utf8
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil

class Cut(PreviewRequest):
    def saveRecord(self, data):
        requestUtil.openDocHook("房间管理-视频剪裁", self.dbUtil, ["rooms"])
        return self.post("console/cut/save-record", data)

    def mergeRecord(self, data):
        requestUtil.openDocHook("媒资管理-视频剪裁-生成回放", self.dbUtil, ["rooms"])
        return self.post("console/cut/merge-record", data)

    def list(self, data):
        requestUtil.openDocHook("媒资管理-视频剪裁-点播列表", self.dbUtil, [])
        return self.post("console/cut/list", data)

    def getVodInfo(self, data):
        requestUtil.openDocHook("媒资管理-视频剪裁-获取点播详情", self.dbUtil, [])
        return self.post("console/cut/get-vod-info", data)
