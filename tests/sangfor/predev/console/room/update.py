#!/usr/bin/env python
# encoding:utf8
import time
import datetime
from PIL import Image
from app.preview.picolive.console.room import *
from utils.config_util import configUtil

testObj = Room("dev_csces_api")
testObj.setDbSection("dev_csces_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

imageUrl = configUtil.get('env', 'image_path')
#image = Image.open(imageUrl)
#with open(imageUrl,"rb") as f:
    #img_bin = f.read() #内容读取
addParam = {
    "name": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
    "il_id": 1,
    "status": 0,
    "changeimg": 1,
    "begin_time": (datetime.datetime.now()+datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S"),
    "begin_time_stamp": int(time.time()),
    "introduction": "<p>" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "</p>",
    "introduction": '',
    "show_chat" : 1,
    "show_duration" : 30,
    "notice_time" : "2021-08-15 10:46:30",
    "guest_ids" : "2,3",
    "assistant_ids" : "4,6,5",
    "audience_ids" : "7,8,9",
    "limit_type" : 2
}
testObj.roomUpdate(addParam, imageUrl)
