#!/usr/bin/env python
#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.master.room import *
from utils.config_util import configUtil
from utils.time_util import timeUtil

testObj = Room("dev_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录
token = configUtil.get(testObj.section, "console_token")

testObj.setCommonData({'vss_token': token})

# 用户开启直播
roomstartLive = {
    'room_id': 'lss_65c1ebcd',
    'start_type': 1,
    'from': 'js'
}
#testObj.startLive(roomstartLive);

# 保存商品显/隐性
saveGoodsDisplay = {
    'room_id': 'lss_65c1ebcd',
    'account_id': '32',
    'operator': '飞翔的鱼',
    'show_goods': 1,
    'client': 'ios',
    'from': 'js'
}
# testObj.saveGoodsDisplay(saveGoodsDisplay)