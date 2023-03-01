#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Chapter(PreviewRequest):
    def get(self, data):
        requestUtil.openDocHook("获取章节", self.dbUtil, ["record"])
        return self.post("console/chapter/get-document-chapter", data)

    def getBatchVodInfos(self, data):
        requestUtil.openDocHook("获取视频信息章节", self.dbUtil, ["record"])
        return self.post("console/chapter/get-batch-vod-infos", data)

    def getVodChapter(self, data):
        requestUtil.openDocHook("获取视频信息章节", self.dbUtil, ["record"])
        return self.post("console/chapter/get-vod-chapter", data)

    def createVodChapter(self, data):
        requestUtil.openDocHook("创建视频信息章节", self.dbUtil, ["record"])
        return self.post("console/chapter/create-vod-chapter", data)

    def updateVodChapter(self, data):
        requestUtil.openDocHook("更新视频信息章节", self.dbUtil, ["record"])
        return self.post("console/chapter/update-vod-chapter", data)

    def deleteVodChapter(self, data):
        requestUtil.openDocHook("删除视频信息章节", self.dbUtil, ["record"])
        return self.post("console/chapter/delete-vod-chapter", data)