#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.console.watchlimit import *
from utils.config_util import configUtil
from utils.time_util import timeUtil

testObj = WatchLimit("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")

whiteloginParam = {
    'whitename': 'test_001',
    'whitepaas': '123456',
    'il_id' : '131',
}
testObj.whitelogin(whiteloginParam)