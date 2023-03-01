#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.vhallapp.console.room import *
from utils.config_util import configUtil

testObj = Room("dev_vhallapp_api")
testObj.setDbSection("dev_vhallapp_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

imageUrl = configUtil.get('env', 'image_path')
image = Image.open(imageUrl)
with open(imageUrl,"rb") as f:
    img_bin = f.read() #内容读取
testObj.setCommonData({'token': token})
addParam = {
    "name": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
    "changeimg": 1,
    "begin_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
    "begin_time_stamp": 1626752990,
    "introduction": "<p>" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "</p>",
    "show_chat" : 1,
    "show_duration" : 30,
    #"notice_time" : "2021-08-15 10:46:29",
    "guest_ids" : "2,3",
    "assistant_ids" : "4,6,5",
    "audience_ids" : "7,8,9",
    "limit_type" : 2
}
testObj.roomCreate(addParam, imageUrl)
