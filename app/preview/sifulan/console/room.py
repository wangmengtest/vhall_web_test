#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil

class Room(PreviewRequest):
    def roomCreate(self, data):
        requestUtil.openDocHook("房间管理-创建房间", self.dbUtil, ["rooms"])
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
        requestUtil.openDocHook("房间管理-我创建的房间列表", self.dbUtil, ["rooms", "room_join"])
        return self.post("console/room/owner-list", data)

    def manageList(self, data):
        requestUtil.openDocHook("房间管理-管理房间列表", self.dbUtil, ["rooms", "room_join"])
        return self.post("console/room/manage-list", data)

    def roomWatchList(self, data):
        requestUtil.openDocHook("观看端口-房间列表", self.dbUtil, ["rooms", "room_join"], False)
        return self.post("console/room/watch-list", data)

    def firstRoomWatchList(self, data):
        requestUtil.openDocHook("观看端口-房间列表", self.dbUtil, ["rooms", "room_join"])
        return self.post("console/room/first-watch-list", data)

    def roomInvitedList(self, data):
        requestUtil.openDocHook("房间管理-我参加的房间列表", self.dbUtil, ["rooms", "room_invited"])
        return self.post("console/room/invited-list", data)

    def roomInvitedCount(self, data):
        requestUtil.openDocHook("房间管理-我参加的房间数量", self.dbUtil, ["rooms", "room_invited"])
        return self.post("console/room/invited-count", data)

    def roomOwnerCount(self, data):
        requestUtil.openDocHook("房间管理-我创建的房间数量", self.dbUtil, ["rooms", "room_invited"])
        return self.post("console/room/owner-count", data)

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

    def endLive(self, data):
        requestUtil.openDocHook("直播间-结束直播", self.dbUtil, ["rooms"], False)
        return self.post("v2/room/end-live", data)

    def getAttributes(self, data):
        requestUtil.openDocHook("直播间-获取房间属性接口", self.dbUtil, ["rooms"], False)
        return self.post("v2/room/get-attributes", data)

    def getRoomInvited(self, data):
        requestUtil.openDocHook("控制台-获取房间邀请信息", self.dbUtil, ["rooms"], False)
        return self.post("console/room/get-room-invited", data)

    def checkRoomPassword(self, data):
        requestUtil.openDocHook("检查房间口令", self.dbUtil, ["rooms", "room_invited"])
        return self.post("console/room/check-room-password", data)

