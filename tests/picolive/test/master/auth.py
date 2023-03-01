#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.master.auth import *
from utils.random_util import randomUtil

testObj = Auth("test_pingan_api")
testObj.setDbSection("dev_picolive_db")


doLoginParam = {
    "phone": randomUtil.mobile(),
    "nickname": randomUtil.nickname(),
    "avatar": "https://m.stg.pingan.com/image/02/4699a2f0e5fb4a279eb5e72bad08191e.jpg",
}
testObj.doLogin()
