#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Exhibition(PreviewRequest):
    def allUser(self, data):
        requestUtil.openDocHook("同步中建用户", self.dbUtil, [])
        return self.post("wUser/selectUserAll", data)

    def allOrg(self, data):
        requestUtil.openDocHook("同步中建组织", self.dbUtil, [])
        return self.get("wOrgOrgs/selectIOrgAll", data)

    def getMaxDurationLive(self, data):
        requestUtil.openDocHook("提供该场会议（指定事件活动）每个观众，观看直播时长最长的场次", self.dbUtil, [])
        return self.get("api/exhibition/get-max-duration-live", data)

    def getMaxDurationLiveHasHeader(self, data, header):
        requestUtil.openDocHook("提供该场会议（指定事件活动）每个观众，观看直播时长最长的场次", self.dbUtil, ["record"])
        return self.postAppendHeader("api/exhibition/get-max-duration-live", data, header)

    def getConcurrencyDetailsHeader(self, data, header):
        requestUtil.openDocHook("并发详情接口", self.dbUtil, ["record"])
        return self.postAppendHeader("api/exhibition/get-concurrency-details", data, header)

    def getLiveDetailHeader(self, data, header):
        requestUtil.openDocHook("直播观看详情接口", self.dbUtil, ["record"])
        return self.postAppendHeader("api/exhibition/get-live-detail", data, header)

    def getRecordDetailHeader(self, data, header):
        requestUtil.openDocHook("回放数据详情接口", self.dbUtil, ["record"])
        return self.postAppendHeader("api/exhibition/get-record-detail", data, header)

    def getQaDataHeader(self, data, header):
        requestUtil.openDocHook("问卷详情数据", self.dbUtil, ["record"])
        return self.postAppendHeader("api/exhibition/get-qa-data", data, header)

    def getQaListHeader(self, data, header):
        requestUtil.openDocHook("问答统计列表接口", self.dbUtil, ["record"])
        return self.postAppendHeader("api/exhibition/get-qa-list", data, header)

    def getRecordDataHeader(self, data, header):
        requestUtil.openDocHook("问答统计列表接口", self.dbUtil, ["record"])
        return self.postAppendHeader("api/stat/get-record-data", data, header)