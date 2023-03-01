#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.watch.qa import *
from utils.config_util import configUtil

testObj = Qa("test_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
app_token = configUtil.get(testObj.section, "app_token")
testObj.setCommonData({'token': app_token})
testObj.setSignRequest()

lists = {
    "room_id": "lss_8ff68147",
    "page_size": "20",
    "status": "0",
    "role": "2",
    # "start_time": "",
    # "end_time": "",
    "sort": "asc",
    "curr_page": "1",
}
testObj.lists(lists)
