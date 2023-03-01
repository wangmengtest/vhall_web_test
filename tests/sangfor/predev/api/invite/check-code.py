#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.meeting.console.invite import *
from utils.config_util import configUtil

testObj = Invite("dev_meeting_api")
testObj.setDbSection("dev_meeting_db")

feAuthData = {
    "il_id": "1",
    'username':'test3@qq.com',
    'code':'123457',
    #"from":'js',
    'en':1
}
imageUrl = configUtil.get('env', 'invite_path')

token = configUtil.get(testObj.section, "console_token")
#testObj.setCommonData({'token': token})
#testObj.setCommonData({'token': '66a602ded2a7f963'})
testObj.verifyCode(feAuthData)