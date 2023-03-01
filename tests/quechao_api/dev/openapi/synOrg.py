#!/usr/bin/env python
# encoding:utf8

from app.preview.huawei.openapi.csces import *
from utils.config_util import configUtil

testObj = Csces("csces_api")
testObj.setDbSection("dev_csces_db")
params = {
}
testObj.allOrg(params)
