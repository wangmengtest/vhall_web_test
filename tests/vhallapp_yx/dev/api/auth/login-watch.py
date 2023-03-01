#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.csces.console.auth import *
from utils.config_util import configUtil

testObj = Auth("dev_vhallapp_api")
testObj.setDbSection("dev_vhallapp_db")

feAuthData = {
    "phone":18519184445,
    "username": "liuweifei",
    "password": "liuyh@140203",
    'code':123456,
    'nickname':'测试',
    'nick_name':'测试',
    'from':'js'
}
testObj.loginWatch(feAuthData)
