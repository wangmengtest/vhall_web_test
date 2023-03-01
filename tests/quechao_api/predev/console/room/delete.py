#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.picolive.console.room import *
from utils.config_util import configUtil

testObj = Room("dev_csces_api")
testObj.setDbSection("dev_csces_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

imageUrl = configUtil.get('env', 'image_path')
image = Image.open(imageUrl)
with open(imageUrl,"rb") as f:
    img_bin = f.read() #内容读取
addParam = {
    "il_id": 2,
    "account_id": 1,
}
testObj.roomDelete(addParam, imageUrl)
