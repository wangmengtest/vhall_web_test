#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.meeting.watch.auth import *
from utils.config_util import configUtil

testObj = Auth("dev_guozhan_api")
testObj.setDbSection("dev_guozhan_db")

feAuthData = {
    "username": "18511337166",
    "code": "309553",
    'live_type':'live',
    'live_lang':'cn',
    'il_id':5906
}
testObj.doLogin(feAuthData, "console_token")

token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})
