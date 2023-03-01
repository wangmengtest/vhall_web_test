#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.vhallapp.watch.auth import *
from utils.config_util import configUtil

testObj = Auth("dev_vhallapp_api")
testObj.setDbSection("dev_vhallapp_db")

feAuthData = {
    "phone":18519184445,
    "nick_name": "liuweifei",
    "type": "2",
    'code':123456,
    'login_type':'3',
    'password':'123456',
    'room_id':'lss_c3868a51',
    'from':'js'
}
testObj.loginAssistant(feAuthData)
