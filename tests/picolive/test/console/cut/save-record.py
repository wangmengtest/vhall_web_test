#!/usr/bin/env python
# encoding:utf8
import json
from app.preview.picolive.console.cut import *
from utils.config_util import configUtil

testObj = Cut("test_picolive_api")
testObj.setDbSection("dev_picolive_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

recordParam = {
    "il_id": 172,
    "vod_id": "9fdc7b90",
    "cut_sections": json.dumps([{"start": 0, "end": 288}, {"start": 972, "end": 5108}]),
    "stream_id": "lss_d4d3af97",
    "point_sections": json.dumps([{"msg": "开始打点", "picurl": "", "timePoint": 0}, {"msg": "1", "picurl": "", "timePoint": 4},
                       {"msg": "打一个点", "picurl": "", "timePoint": 10}, {"msg": "开始打点", "picurl": "", "timePoint": 42},
                       {"timePoint": 290, "msg": "打点1"}, {"timePoint": 578, "msg": "打点2"},
                       {"timePoint": 809, "msg": "打点3"}]),
    "cut_type": 0,
    "name": "打点剪辑测试",
}
testObj.saveRecord(recordParam)
