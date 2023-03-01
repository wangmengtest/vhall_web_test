#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.vhallapp.watch.auth import *
from utils.config_util import configUtil

testObj = Auth("dev_vhallapp_api")
testObj.setDbSection("dev_vhallapp_db")

feAuthData = {
    "phone": "18519184446",
    "username": "liuweifei",
    "nick_name": "liuweifei",
    "password": "liuyh@140203",
    "from":"js"
}
testObj.loginWatch(feAuthData, "console_token")
