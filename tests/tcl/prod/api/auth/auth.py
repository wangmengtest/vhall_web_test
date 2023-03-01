#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.csces.console.auth import *
from utils.config_util import configUtil

testObj = Auth("prod_csces_api")
testObj.setDbSection("dev_csces_db")

feAuthData = {
    "username": "liuweifei",
    "password": "liuyh@140203",
}
testObj.doLogin(feAuthData, "console_token")
