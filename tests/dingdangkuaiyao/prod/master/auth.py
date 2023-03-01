#!/usr/bin/env python
# encoding:utf8

from app.preview.csces.master.auth import *
from utils.random_util import randomUtil

testObj = Auth("prod_pingan_api")
testObj.setDbSection("dev_csces_db")


doLoginParam = {
    "phone": randomUtil.mobile(),
    "nickname": randomUtil.nickname(),
    "avatar": "https://m.stg.csces.com/image/02/4699a2f0e5fb4a279eb5e72bad08191e.jpg",
}
testObj.doLogin()
