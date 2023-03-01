#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.watch.auth import *
from utils.random_util import randomUtil

testObj = Auth("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")

# 设置登录信息
testObj.setSignRequest()

audicnceAuthData = {
    "third_party_user_id": randomUtil.thirdPartyUserId(),
    "nickname": randomUtil.nickname(),
    "avatar": "https://m.stg.pingan.com/image/02/4699a2f0e5fb4a279eb5e72bad08191e.jpg",
}
testObj.doLogin(audicnceAuthData, "app_token")
