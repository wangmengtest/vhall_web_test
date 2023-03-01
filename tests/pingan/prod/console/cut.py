# #!/usr/bin/env python
# encoding:utf8

import json
from app.preview.pingan.console.cut import *
from utils.config_util import configUtil
from utils.time_util import timeUtil

testObj = Cut("prod_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

saveRecordParams = {
    "il_id": 1100000876,
    "vod_id": "83fba852",
    "cut_sections": json.dumps([{"start": 0, "end": 288}, {"start": 972, "end": 5108}]),
    "stream_id": "lss_a5236d75",
    "point_sections": json.dumps([{"msg": "开始打点", "picurl": "", "timePoint": 0}, {"msg": "1", "picurl": "", "timePoint": 4},
                       {"msg": "打一个点", "picurl": "", "timePoint": 10}, {"msg": "开始打点", "picurl": "", "timePoint": 42},
                       {"timePoint": 290, "msg": "打点1"}, {"timePoint": 578, "msg": "打点2"},
                       {"timePoint": 809, "msg": "打点3"}]),
    "cut_type": 0,
    "name": "打点剪辑测试",
}

testObj.saveRecord(saveRecordParams)