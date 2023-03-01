#!/usr/bin/env python
# encoding:utf8

from app.preview.huawei.openapi.tobhuawei import *
from utils.config_util import configUtil

testObj = Tob("dev_huawei_tob_api")
testObj.setDbSection("dev_huawei_db")
params = {
    'liveId':'10000'
}
testObj.highlightMyConcern(params, {'X-HW-ID':'com.huawei.it.ioc','X-HW-APPKEY':'T96nzDX7k9pJHD13a8p22w==','token':'6b48f504c5f6e773','referer':'https://vhall-test.huawei.com'})
