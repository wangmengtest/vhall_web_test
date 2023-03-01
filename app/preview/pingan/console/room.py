#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil

class Room(PreviewRequest):
    def roomCreate(self, data, path=None):
        requestUtil.openDocHook("房间管理-创建房间", self.dbUtil, ["rooms"], False)

        if path:
            return self.upload("console/room/create", 'image', path, data)
        else:
            return self.post("console/room/create", data)

    def saveBullet(self, data):
        requestUtil.openDocHook("房间管理-控制弹幕", self.dbUtil, ["rooms","room_supply"])
        return self.post("console/room/save-bullet", data)        

    def roomUpdateStatus(self, data):
        requestUtil.openDocHook("房间管理-修改房间状态", self.dbUtil, ["rooms"])
        return self.post("console/room/update-status", data)

    def roomInfo(self, data):
        requestUtil.openDocHook("房间管理-房间信息", self.dbUtil, ["rooms", "room_join"], False)
        return self.post("console/room/get", data)

    def inavGet(self, data):
        requestUtil.openDocHook("房间管理-房间信息", self.dbUtil, ["rooms", "room_join"], False)
        return self.post("api/inav/get", data)        

    def competence(self, data):
        requestUtil.openDocHook("房间管理-权限分配信息", self.dbUtil, ["rooms", "room_join"], False)
        return self.post("console/room/get-competence", data)

    def roomList(self, data):
        requestUtil.openDocHook("房间管理-列表", self.dbUtil, ["rooms", "room_join"])
        return self.post("console/room/list", data)

    def thirdartyTags(self):
        requestUtil.openDocHook("获取标签类型", self.dbUtil, ["tag"], False)
        return self.post("console/room/third-party-tags", {})

    def tagList(self, data):
        requestUtil.openDocHook("获取标签列表", self.dbUtil, ["tag"], False)
        return self.post("console/tag/list", data)

    def getInviteCode(self, data):
        requestUtil.openDocHook("控制台-房间-获取邀请码", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("console/room/get-invite-code", data)

    def saveInviteCode(self, data):
        requestUtil.openDocHook("控制台-房间-保存邀请码 v2.0", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("/console/room/save-invite-code", data)

    def pushStream(self, data):
        requestUtil.openDocHook("控制台-房间-创建一个拉取第三方流的配置 v2.0", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("/console/room/push-stream", data)

    def getPushStream(self, data):
        requestUtil.openDocHook("控制台-房间-获取推流地址 v2.0", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("/console/room/get-stream-address", data)

    def setLiveRecord(self, data):
        requestUtil.openDocHook("控制台-房间-关联违直播 v2.1.0", self.dbUtil, ["room_record_lk","rooms", "record"], False)
        return self.post("console/room/set-live-record", data)

    def liveRecordInfo(self, data):
        requestUtil.openDocHook("控制台-房间-违直播详情 v2.1.0", self.dbUtil, ["room_record_lk","rooms", "record"], False)
        return self.post("console/room/live-record-info", data)            

    def rePushLiveRecord(self, data):
        requestUtil.openDocHook("控制台-房间-重推违直播 v2.1.0", self.dbUtil, ["room_record_lk","rooms", "record"], False)
        return self.post("console/room/re-push-live-record", data)

    def deleteLiveRecord(self, data):
        requestUtil.openDocHook("控制台-房间-删除违直播 v2.1.0", self.dbUtil, ["room_record_lk","rooms", "record"], False)
        return self.post("console/room/delete-live-record", data)     
                           