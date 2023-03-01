#!/usr/bin/env python
# encoding:utf8

from app.preview.huawei.openapi.tob import *
from utils.config_util import configUtil

testObj = Tob("dev_huawei_api")
testObj.setDbSection("dev_huawei_db")
params = {
}
testObj.verifyToken(params)
