#!/usr/bin/env python
# encoding:utf8
import json

from app.preview.picolive.console.gift import *
from utils.config_util import configUtil

testObj = Gift("test_picolive_api")
testObj.setDbSection("dev_picolive_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

addParam = {
    "gift_id":114,
    #"room_id":'lss_9043fd5a',
    "room_id":'lss_ce01842a',
    "vss_token":"access:b6f14dbf:abedffb6998f8671",
    "quantity":1,
    "en": "1",
}
ret = testObj.send(addParam)
json_str = json.dumps(ret)
json.loads(json_str)

