#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil

class Question(PreviewRequest):
    def create(self, data):
        requestUtil.openDocHook("控制台-创建问卷 V2.1.0", self.dbUtil, ["question"])
        return self.post("console/question/create", data)

    def update(self, data):
        requestUtil.openDocHook("控制台-更新问卷 V2.1.0", self.dbUtil, ["question"])
        return self.post("console/question/update", data)

    def detail(self, data):
        requestUtil.openDocHook("控制台-问卷详情 V2.1.0", self.dbUtil, ["question"])
        return self.post("console/question/get", data)        

    def lists(self, data):
        requestUtil.openDocHook("控制台-问卷列表 V2.1.0", self.dbUtil, ["question"])
        return self.post("console/question/list", data)    

    def delete(self, data):
        requestUtil.openDocHook("控制台-删除问卷 V2.1.0", self.dbUtil, ["question"])
        return self.post("console/question/delete", data)

    def publish(self, data):
        requestUtil.openDocHook("控制台-发布问卷 V2.1.0", self.dbUtil, ["question"])
        return self.post("console/question/publish", data)

    def linkRoom(self, data):
        requestUtil.openDocHook("控制台-关联问卷列表 V2.1.0", self.dbUtil, ["question"])
        return self.post("console/question/link-room-list", data)

    def unbindRoom(self, data):
        requestUtil.openDocHook("控制台-解绑问卷 V2.1.0", self.dbUtil, ["question"])
        return self.post("console/question/batch-unbind-room", data)

    def export(self, data):
        requestUtil.openDocHook("控制台-导出问卷 V2.1.0", self.dbUtil, ["question"])
        return self.post("console/question/export-question-answer", data)                                        
