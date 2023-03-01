#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.meeting.watch.auth import *
from utils.config_util import configUtil

testObj = Auth("test_meeting_api")
testObj.setDbSection("dev_meeting_db")

feAuthData = {
    "username": "18519184446",
    "code": "309553",
}
testObj.doLogin(feAuthData, "console_token")

token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})
