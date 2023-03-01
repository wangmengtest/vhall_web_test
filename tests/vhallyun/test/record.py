#!/usr/bin/env python
# encoding:utf8

from app.vhallyun.record import *
from utils.time_util import timeUtil

testObj = Record("test_pingan_vhallyun_api")

transCodeParams = {
    'vod_id': "835e9a94",
    'quality': '360p,480p,720p',
}
# result = testObj.transCode(transCodeParams)