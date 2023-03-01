#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.picolive.v2.document import *
from utils.config_util import configUtil

testObj = Document("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")
token = configUtil.get(testObj.section, "console_token")
vssToken = configUtil.get(testObj.section, "vss_token")
testObj.setCommonData({'vss_token':vssToken})
params = {
    "room_id": 'test',
    "receive_account_id":1,
    'from':'js'
}
testObj.agreeInvite(params)
