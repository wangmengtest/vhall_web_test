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

    def setRelatedVod(self, data):
        requestUtil.openDocHook("内容-设置精彩瞬间 v2.0", self.dbUtil, ["record"])
        return self.post("console/record/set-related-vod", data)

    def setShowChapter(self, data):
        requestUtil.openDocHook("房间-回放管理-章节-显示章节目录开关", self.dbUtil, ["record"])
        return self.post("console/record/set-show-chapter", data)

    def getRelatedVod(self, data):
        requestUtil.openDocHook("内容-获取精彩瞬间 v2.0", self.dbUtil, ["record"])
        return self.post("api/record/get-related-vod", data)

    def update(self, data):
        requestUtil.openDocHook("内容-回放编辑", self.dbUtil, ["record"])
        return self.post("console/record/update", data)

    def submitTranscodeTasks(self, data):
        requestUtil.openDocHook("内容-回放编辑", self.dbUtil, ["record"])
        return self.post("api/record/submit-transcode-tasks", data)

    def list(self, data):
        requestUtil.openDocHook("内容-回放 v2.0", self.dbUtil, ["record"])
        return self.post("console/record/list", data)

    def createToken(self, data):
        requestUtil.openDocHook("内容-回放 v2.0", self.dbUtil, ["record"])
        return self.post("console/recordsharetokens/save", data)