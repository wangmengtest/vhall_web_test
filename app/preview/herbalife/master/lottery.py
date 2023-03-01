#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil


class Lottery(PreviewRequest):
    def importTemplate(self, data):
        requestUtil.openDocHook("抽奖管理-下载抽奖模板", self.dbUtil, ["rooms"])
        return self.get("v4/lottery/import-template", data)

    def importUser(self, data, filePath):
        requestUtil.openDocHook("控制台-抽奖-导入自定义抽奖人 v2.0", self.dbUtil, ["room_lottery", "lottery_user"], False)
        return self.upload("v4/lottery/import-user", "lottery_users", filePath, data)

    def lotterySearch(self, data):
        requestUtil.openDocHook("控制台-抽奖-搜索符合范围条件的抽奖用户名单 v2.0", self.dbUtil, ["room_lottery", "lottery_user"], False)
        return self.post("v4/lottery/search", data)

    def lotteryAdd(self, data):
        requestUtil.openDocHook("控制台-抽奖-发起抽奖 v2.0", self.dbUtil, ["room_lottery", "lottery_user"], False)
        return self.post("v4/lottery/add", data)

    def lotteryPublish(self, data):
        requestUtil.openDocHook("控制台-抽奖-公布抽奖结果 v2.0", self.dbUtil, ["room_lottery", "lottery_user"], False)
        return self.post("v4/lottery/publish", data)

