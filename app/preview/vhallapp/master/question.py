#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil

class Question(PreviewRequest):
    def getAccessToken(self, data):
        requestUtil.openDocHook("控制台&主播&助理-获取AccessToken V2.1.0", self.dbUtil, ["question"])
        return self.post("v2/question/get-access-token", data)        

    def create(self, data):
        requestUtil.openDocHook("主播&助理-创建问卷 V2.1.0", self.dbUtil, ["question"])
        return self.post("v2/question/create", data)        

    def delete(self, data):
        requestUtil.openDocHook("主播&助理-删除问卷 V2.1.0", self.dbUtil, ["question"])
        return self.post("v2/question/deleted", data)

    def info(self, data):
        requestUtil.openDocHook("主播&助理-问卷详情 V2.1.0", self.dbUtil, ["question"])
        return self.post("v2/question/info", data)           

    def repush(self, data):
        requestUtil.openDocHook("主播&助理-问卷推屏 V2.1.0", self.dbUtil, ["question"])
        return self.post("v2/question/repush", data)   

    def publish(self, data):
        requestUtil.openDocHook("主播&助理-发布问卷 V2.1.0", self.dbUtil, ["question"])
        return self.post("v2/question/publish", data)           
 
    def cancelPublish(self, data):
        requestUtil.openDocHook("主播&助理-取消发布问卷 V2.1.0", self.dbUtil, ["question"])
        return self.post("v2/question/cancel-publish", data)            

    def copy(self, data):
        requestUtil.openDocHook("主播&助理-拷贝问卷 V2.1.0", self.dbUtil, ["question"])
        return self.post("v2/question/copy", data)        

    def update(self, data):
        requestUtil.openDocHook("主播&助理-更新问卷 V2.1.0", self.dbUtil, ["question"])
        return self.post("v2/question/update", data)             

    def unbindRoom(self, data):
        requestUtil.openDocHook("主播&助理-解绑问卷 V2.1.0", self.dbUtil, ["question"])
        return self.post("v2/question/unbind-room", data)        

    def update(self, data):
        requestUtil.openDocHook("主播&助理-更新问卷 V2.1.0", self.dbUtil, ["question"])
        return self.post("v2/question/update", data)                        

    def lists(self, data):
        requestUtil.openDocHook("观众-问卷列表 V2.1.0", self.dbUtil, ["question"])
        return self.post("v2/question/list", data)            

    def info(self, data):
        requestUtil.openDocHook("观众-问卷详情 V2.1.0", self.dbUtil, ["question"])
        return self.post("v2/question/info", data)       