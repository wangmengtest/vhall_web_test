#!/usr/bin/env python
# encoding:utf8

from app.preview.herbalife.master.lottery import *
from utils.config_util import configUtil
from utils.time_util import timeUtil

# testObj = Lottery("test_herbalife_api")
testObj = Lottery("dev_herbalife_api")
testObj.setDbSection("dev_common_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
vss_token = configUtil.get(testObj.section, "vss_token")

testObj.setCommonData({'token': token, 'vss_token': vss_token})


lotterySearchParam = {
    "room_id": "lss_3cde9288",
    "lottery_rule": 2,
    "lottery_type": 9,
    "keyword": "三方用户ID_2"
}
# testObj.lotterySearch(lotterySearchParam)


lotteryAddParam = {
    "room_id": "lss_846ca239",
    "lottery_type": 1,
    "lottery_number": 1,
    "lottery_user_ids": "",
    "lottery_rule_text": "随机抽奖",
    "extension": [],
    "winner_out": 0,
    "end_type": 3,
    "from": "js",
}

for i in range(10):
    testObj.lotteryAdd(lotteryAddParam)
    timeUtil.sleep(1)


