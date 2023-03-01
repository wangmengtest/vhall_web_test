#!/usr/bin/env python
# encoding:utf8
import os
import sys
sys.path.append(f"{os.getcwd()}")
from app.preview.picolive.console.auth import *
from utils.config_util import configUtil
testObj = Auth("test_picolive_api")
#testObj.setDbSection("dev_picolive_db")

feAuthData = {
    "username": "mengmeng1",
    "password": "mengmeng123",
    'type'    : '1'
}
testObj.doLogin(feAuthData, "console_token")

token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})


