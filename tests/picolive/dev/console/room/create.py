#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.picolive.console.room import *
from utils.config_util import configUtil

testObj = Room("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

imageUrl = configUtil.get('env', 'image_path')
image = Image.open(imageUrl)
with open(imageUrl,"rb") as f:
    img_bin = f.read() #内容读取
testObj.setCommonData({'token': token})
addParam = {
    "name": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
    "il_id": 1,
    "changeimg": 1,
    "begin_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
    "begin_time_stamp": 1626752990,
    "introduction": "<p>" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "</p>",
    "lang":1
}
testObj.roomCreateHasImage(addParam, imageUrl)
