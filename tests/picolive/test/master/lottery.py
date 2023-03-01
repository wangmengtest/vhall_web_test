#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.master.lottery import *
from utils.config_util import configUtil

testObj = Lottery("test_pingan_api")
testObj.setDbSection("dev_picolive_db")

# 设置登录信息
vss_token = configUtil.get(testObj.section, "vss_token")
testObj.setCommonData({'vss_token': vss_token})

importTemplateParam = {
    'room_id': 'lss_3cde9288',
}
# importTemplate(importTemplateParam)

importUserParam = {
    "room_id": "lss_3cde9288",
    'time': '1'
}

# testObj.importUser(importUserParam, "/Users/nelsonking/Desktop/lottery_user_list20210531212335.xlsx")
# testObj.importUser(importUserParam, "/Users/nelsonking/Desktop/lottery_user_list20210621201119.xlsx")
# testObj.importUser(importUserParam, "/Users/nelsonking/Desktop/vhall/excel/丢失数据2(1).xlsx")
testObj.importUser(importUserParam, "/Users/nelsonking/Desktop/3000数据.xlsx")

lotteryCountParam = {
    "room_id": "lss_3cde9288",
    "lottery_rule": 2,
    "lottery_type": 6,
    "winner_out": 1,
    "lottery_rule_text": "自定义用户抽奖",
    "from": "js",
}

testObj.lotteryCount(lotteryCountParam)

lotterySearchParam = {
    "room_id": "lss_3cde9288",
    "lottery_rule": 2,
    "lottery_type": 9,
    "keyword": "三方用户ID_2"
}
# testObj.lotterySearch(lotterySearchParam)


lotteryAddParam = {
    "lottery_rule_text": "自定义抽奖测试",
    "room_id": "lss_3cde9288",
    "lottery_rule": 2,
    "lottery_type": 9,
    "lottery_number": 1820,
    "lottery_user_ids": "",
    "show_time": 30,
}
testObj.lotteryAdd(lotteryAddParam)

lotteryPublishParam = {

}
# testObj.lotteryPublish(lotteryPublishParam)

