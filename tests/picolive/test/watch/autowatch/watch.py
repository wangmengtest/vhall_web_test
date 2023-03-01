#!/usr/bin/env python
# encoding:utf8
import time

import app.preview.picolive.console.pendant
from app.preview.picolive.console.gift import *
from app.preview.picolive.watch.room import *
from utils.config_util import configUtil
from utils.web_socket_util import WebSocketUtil
from app.preview.picolive.console.auth import *

testObj = Gift("test_picolive_api")
testObj.setDbSection("dev_picolive_db")
token = configUtil.get(testObj.section, "console_token")
testObj.setCommonData({'token': token})

def browerLogin(ilId):
    #用户登录拿到token account_id
    authObj = Auth("test_picolive_api")
    #testObj.setDbSection("dev_picolive_db")
    feAuthData = {
        "username": "mengmeng1",
        "password": "mengmeng123",
        'type': '1'
    }
    accountInfo = authObj.doLogin(feAuthData, "console_token")

    roomObj = Room("test_picolive_api")
    RoomGetParams = {
        "il_id": ilId,
        "from": "js",
    }
    token = configUtil.get(roomObj.section, 'console_token')
    roomObj.setCommonData({
        'token': token
    })
    roomGetResult = roomObj.roomGet(RoomGetParams)
    #获取accessToken
    print(roomGetResult.get("access_token_url"))
    accessTokenGetUrl = roomGetResult.get("access_token_url")
    accessTokenGetUrlRequest = requestUtil.get(accessTokenGetUrl)
    accessToken = accessTokenGetUrlRequest.get("data").get("access_token")
    configUtil.set(roomObj.section, "access_token", accessToken)

    # SDK初始化
    sdkUrl = "https://api.vhallyun.com/sdk/v1/init/start?app_id=b6f14dbf&client=pc_browser&access_token=" + accessToken + "&package_check=package_check&third_party_user_id=" + str(accountInfo['account_id']) + "&channel_id=ch_xqUad32b"
    sdlInitRequest = requestUtil.get(sdkUrl)
    socketServer = sdlInitRequest['data']['socket_server'] + "?token" + sdlInitRequest['data']['connection_token'] + "&transport=websocket"
    socketServer = "wss://im-connect.vhall.com/socket.io/" + "?token" + sdlInitRequest['data']['connection_token'] + "&transport=websocket"
    print(socketServer)
    socketUtil = WebSocketUtil(socketServer)
    socketUtil.connect()


browerLogin(264)
