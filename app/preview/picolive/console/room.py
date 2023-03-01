#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil

class Room(PreviewRequest):
    def roomCreate(self, data):
        requestUtil.openDocHook("房间管理-创建房间", self.dbUtil, ["rooms"])
        return self.post("console/room/create", data)

    def roomCreateHasImage(self, data, path):
        requestUtil.openDocHook("房间管理-创建房间", self.dbUtil, ["rooms"])
        return self.upload("console/room/create", 'image', path, data)

    def roomUpdate(self, data, path):
        requestUtil.openDocHook("房间管理-更新房间", self.dbUtil, ["rooms"])
        return self.upload("console/room/update", 'image', path, data)

    def roomDelete(self, data, path):
        requestUtil.openDocHook("房间管理-删除房间", self.dbUtil, ["rooms"])
        return self.upload("console/room/delete", 'image', path, data)

    def roomUpdateStatus(self, data):
        requestUtil.openDocHook("房间管理-修改房间状态", self.dbUtil, ["rooms"])
        return self.post("console/room/update-status", data)

    def roomInfo(self, data):
        requestUtil.openDocHook("房间管理-房间信息", self.dbUtil, ["rooms", "room_join"], False)
        return self.post("console/room/get", data)

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
        requestUtil.openDocHook("控制台-房间-创建一个拉取第三方流的配置 v2.0", self.dbUtil, ["rooms", "room_supply"], False)
        return self.post("/console/room/get-stream-address", data)

    def endLive(self, data):
        requestUtil.openDocHook("直播间-结束直播", self.dbUtil, ["rooms"], False)
        return self.post("/v2/room/end-live", data)

    def editStatus(self, data):
        requestUtil.openDocHook("房间管理-修改房间状态", self.dbUtil, ["rooms"])
        return self.post("console/room/edit-status", data)

    def checkRoomPassword(self, data):
        requestUtil.openDocHook("检查房间口令", self.dbUtil, ["rooms", "room_invited"])
        return self.post("console/room/check-room-password", data)
