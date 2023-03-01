#!/usr/bin/env python
# encoding:utf8

import require
from app.preview.preview_request import PreviewRequest
from utils.request_util import requestUtil

class Room(PreviewRequest):
    # 开启直播
    def startLive(self, data):
        requestUtil.openDocHook("开启直播", self.dbUtil, ['rooms', 'room_supply'], False)
        return self.post("/v2/room/start-live", data)

    # 保存商品显隐
    def saveGoodsDisplay(self, data):
        requestUtil.openDocHook("保存商品显隐", self.dbUtil, ['rooms', 'room_supply'], False)
        return self.post("/v2/room/save-goods-display", data)