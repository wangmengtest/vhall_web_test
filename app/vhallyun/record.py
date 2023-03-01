#!/usr/bin/env python
# encoding:utf8

import require
from app.vhallyun.vhallyun_request import VhallYunRequest
from utils.request_util import requestUtil


class Record(VhallYunRequest):
    def transCode(self, data):
        requestUtil.openDocHook("点播转码", None)
        data['action'] = 'SubmitTranscodeTasks'

        return self.post("api/v2/vod", data)

    def videoEdit(self, data):
        requestUtil.openDocHook("提交剪辑任务", None)
        data['action'] = 'SubmitVideoEditTasks'

        return self.post("api/v2/vod", data)

    def getRecordJoinInfo(self, data):
        requestUtil.openDocHook("点播参会详情", None)
        return self.post("api/v1/record/get-record-join-info", data)

    def getVodList(self, data):
        # requestUtil.openDocHook("获取点播列表", self.dbUtil)
        data['action'] = 'GetVodList'
        return self.post("api/v2/vod", data)

    def recordDelete(self, data):
        requestUtil.openDocHook("删除点播", None)
        data['action'] = 'SubmitDeleteVodTasks'
        return self.post("api/v2/vod", data)

    def createRecord(self, data):
        requestUtil.openDocHook("生成点播", None, )
        data['action'] = 'SubmitCreateRecordTasks'
        return self.post("api/v2/vod", data)    
