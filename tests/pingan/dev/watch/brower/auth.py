#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.watch.auth import *

testObj = Auth("dev_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})


audicnceAuthData = {
    "third_party_user_id": "audience_audience_957f76d6c4dd435480e88746fd53ce50",
    "nickname": "用户-1001",
    "avatar": "https://m.stg.pingan.com/image/02/4699a2f0e5fb4a279eb5e72bad08191e.jpg",
}
testObj.doLogin(audicnceAuthData, "app_token")