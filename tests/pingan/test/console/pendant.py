#!/usr/bin/env python
# encoding:utf8

from app.preview.pingan.console.pendant import *
from utils.config_util import configUtil

testObj = Pendant("test_pingan_api")
testObj.setDbSection("dev_pingan_db")

# 设置登录信息
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

createParam = {
    'name': '测试组件添加-地址',
    'content_type': 2,
    'pendant_url': 'https://www.baidu.com',
    'coupon_id': "11abc2/24",
}
testObj.create(createParam, "/Users/nelsonking/Desktop/vhall/img/background.png")


updateParam = {
    'id': 1,
    'name': 1100000478,
    'content_type': 1,
    'pendant_url': 'https://www.baidu.com',
    'coupon_id': 0,
}
# testObj.update(updateParam, "/Users/nelsonking/Desktop/vhall/img/goods-01.png")

deleteParam = {
    "id": 1,
}

# testObj.delete(deleteParam)

getListParam = {
    'keyworkd': "",
    "page": 1,
    "page_size": 10,
}
# gtestObj.etList(getListParam)

pushScreenParams = {
    'il_id': 1100000695,
    'pendant_id': 2,
    'channel_id': 'ch_9f87d47c',
    'screen_second': 60
}
# testObj.pushScreen(pushScreenParams)

getStatListParams = {
    'il_id': 1100000553,
    'page': '1',
    'page_size': '10',
}
# testObj.getStatList(getStatListParams)
