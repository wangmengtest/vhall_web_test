#!/usr/bin/env python
# encoding:utf8

from app.preview.csces.openapi.anchor import *

testObj = Anchor("prod_pingan_api")
testObj.setDbSection("dev_csces_db")

# 设置登录信息
testObj.setSignRequest()

createParam = {
    "nickname": "xiaoshou",
    "password": "123456",
    "profile_img_url": "https://cdn.m.stock.csces.com/image/02/c462e131fb494614b344883bdf355000.jpg",
    "third_party_user_id": "4948946154849",
    "username": "xiaoshou"
}
testObj.create(createParam)

deleteParam = {
    "third_party_user_id": "62c5bb6a25fb4568ba9d041cfbd17826",
    "username": "35242831"
}
# testObj.delete(deleteParam)
