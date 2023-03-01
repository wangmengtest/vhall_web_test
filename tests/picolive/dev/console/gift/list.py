#!/usr/bin/env python
# encoding:utf8
import json

from app.preview.picolive.console.gift import *
from utils.config_util import configUtil

testObj = Gift("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

addParam = {
    "en": "1",
}
ret = testObj.list(addParam)
json_str = json.dumps(ret)
json.loads(json_str)

