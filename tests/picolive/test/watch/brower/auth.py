#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.watch.auth import *
from app.preview.picolive.watch.room import *
from utils.random_util import randomUtil
from utils.request_util import requestUtil

testObj = Auth("test_pingan_api")
testObj.setDbSection("dev_picolive_db")

roomObj = Room("test_pingan_api")
roomObj.setDbSection("dev_picolive_db")

# 设置登录信息
token = configUtil.get(testObj.section, "admin_token")
testObj.setCommonData({'token': token})

audicnceAuthData = {
    "third_party_user_id": "audience_audience_957f76d6c4dd435480e88746fd53ce50",
    "nickname": "用户-1001",
    "avatar": "https://m.stg.pingan.com/image/02/4699a2f0e5fb4a279eb5e72bad08191e.jpg",
}


# testObj.doLogin(audicnceAuthData, "app_token")


def browerLogin(ilId, password):
    doIdentifyLoginParam = {
        "phone": randomUtil.mobile(),
        "nickname": randomUtil.nickname(),
        "code": 123456,
        "password": password,
        "il_id": ilId,
        "from": "js",
    }
    # 获取用户创建TOKEN
    result = testObj.doIdentifyLogin(doIdentifyLoginParam, "identify_token")

    saveUserUrl = result.get("data").get("save_user_url")
    # 保存频道用户信息
    result = requestUtil.get(saveUserUrl)

    # 获取房间信息
    identifyToken = configUtil.get(roomObj.section, 'identify_token')
    roomObj.setCommonData({
        'token': identifyToken
    })
    RoomGetParams = {
        "il_id": ilId,
        "from": "js",
    }
    roomGetResult = roomObj.roomGet(RoomGetParams)

    # 获取accessToken
    accessTokenGetUrl = roomGetResult.get("data").get("access_token_url")
    accessTokenGetUrlRequest = requestUtil.get(accessTokenGetUrl)
    accessToken = accessTokenGetUrlRequest.get("data").get("access_token")
    configUtil.set(roomGetResult.section, "access_token", accessToken)

    # SDK初始化


    print(accessTokenGetUrlRequest)


browerLogin(1100000893, 303893)
