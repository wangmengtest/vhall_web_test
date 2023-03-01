#!/usr/bin/env python
# encoding:utf8
import time
from PIL import Image
from app.preview.picolive.console.gift import *
from utils.config_util import configUtil

testObj = Gift("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

imageUrl = configUtil.get('env', 'image_path')
image = Image.open(imageUrl)
with open(imageUrl,"rb") as f:
    img_bin = f.read() # 内容读取
addParam = {
    "name": time.time(),
    #"image": img_bin
}
testObj.add(addParam, imageUrl)
