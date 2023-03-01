#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.picolive.v2.lottery import *
from utils.config_util import configUtil

testObj = Lottery("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")
token = configUtil.get(testObj.section, "console_token")
vssToken = configUtil.get(testObj.section, "vss_token")
lotteryUserIds = configUtil.get(testObj.section, "lottery_user_ids")
testObj.setCommonData({'token': token, 'vss_token':vssToken, 'lottery_user_ids':lotteryUserIds})

param = {
    "from" : 'js',
    "room_id" : 'test',
    'lottery_rule':2,
    'lottery_type':1,
    'lottery_number':1,
    'lottery_rule_text':1,
    'third_party_user_id':22
}
testObj.add(param)

