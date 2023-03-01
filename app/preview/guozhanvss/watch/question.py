#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil

class Question(PreviewRequest):
    def submit(self, data):
        requestUtil.openDocHook("观众-提交问卷 V2.1.0", self.dbUtil, ["question"])
        return self.post("/v2/question/answer", data)
    
    def checkAnswered(self, data):
        requestUtil.openDocHook("观众-检查是否提交过问卷 V2.1.0", self.dbUtil, ["question"])
        return self.post("/v2/question/check-survey", data)

    def getQuestionDetail(self, data):
        requestUtil.openDocHook("观众-获取提交详情 V2.1.0", self.dbUtil, ["question"])
        return self.post("/v2/question/submit-info", data)

    def getQuestionNum(self, data):
        requestUtil.openDocHook("观众-获取问卷数量 V2.1.0", self.dbUtil, ["question"])
        return self.post("/v2/question/get-num", data)   

    def watchList(self, data):
        requestUtil.openDocHook("观众-问卷列表 V2.1.0", self.dbUtil, ["question"])
        return self.post("/v2/question/watch-list", data)   
