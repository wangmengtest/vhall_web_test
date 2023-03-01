#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil
from utils.config_util import configUtil
from utils.log_util import logUtil


class Lottery(PreviewRequest):
    def test(self, data):
        requestUtil.openDocHook("抽奖-test", self.dbUtil, [])
        return self.post("v2/lottery/test", data)

    def lotteryable(self, data):
        requestUtil.openDocHook("抽奖-是否可以发起抽奖", self.dbUtil, [])
        return self.post("v2/lottery/lotteryable", data)

    def add(self, data, option = 'lottery_id'):
        requestUtil.openDocHook("抽奖-发起抽奖", self.dbUtil, [])
        result = self.post("v2/lottery/add", data)
        result = self.parseResult(result)
        lotteryId = result.get('id')
        configUtil.set(self.section, option, str(lotteryId))
        logUtil.renderConsole(lotteryId)

    def end(self, data):
        requestUtil.openDocHook("抽奖-结束抽奖", self.dbUtil, [])
        return self.post("v2/lottery/end", data)

    def importUser(self, data, path):
        requestUtil.openDocHook("抽奖-自定义中奖用户", self.dbUtil, [])
        return self.upload("v2/lottery/import-user", 'lottery_users', path, data)

    def count(self, data):
        requestUtil.openDocHook("抽奖-获取可以中奖人数", self.dbUtil, [])
        return self.post("v2/lottery/count", data)

    def search(self, data, option = 'lottery_user_ids'):
        requestUtil.openDocHook("抽奖-指定中奖人", self.dbUtil, [])
        result = self.post("v2/lottery/search", data)
        result = self.parseResult(result)
        lotteryUserIds = str(result['list'][0].get('id'));
        configUtil.set(self.section, option, lotteryUserIds)
        logUtil.renderConsole(lotteryUserIds)

    def publish(self, data):
        requestUtil.openDocHook("抽奖-公布结果", self.dbUtil, [])
        return self.post("v2/lottery/publish", data)
