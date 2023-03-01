#!/usr/bin/env python
# encoding:utf8

import require
import json
import urllib.parse
from utils.web_socket_util import WebSocketUtil
from utils.log_util import logUtil

url = "wss://chat01.e.vhall.com/ws/ch_UwVEf0pG?date=1626964050220&_=1626964050220&tag=&time=&eventid="
socketUtil = WebSocketUtil(url)
def parseMessage(message):
    data = json.loads(message)
    logUtil.renderConsole(data.get("text"))
    data = urllib.parse.unquote(data.get("text"))
    logUtil.renderConsole(data)


socketUtil.setOnMessage(lambda ws, message: (
    logUtil.renderConsole("on message"),
    parseMessage(message),
))
socketUtil.connect()


# url = "wss://im-connect.vhall.com/socket.io/?token=ad133b75d9e54856a06f61d4a02df73f&ip=vhallim-connect06-online-ali-bje.vhouhn.com&port=8005&channelId=ch_UwVEf0pG&userId=101&appId=b7eb60bc&client=pc_browser&role=host&version=v3&EIO=3&transport=websocket"
# socketUtil = WebSocketUtil(url)
#
# template = "42[&quot;join&quot;,{&quot;channel&quot;:&quot;${channelId}&quot;,&quot;third_party_user_id&quot;:&quot;${third_party_user_id}&quot;,&quot;context&quot;:&quot;{\&quot;nickname\&quot;:\&quot;${nickname}\&quot;,\&quot;device_t     ype\&quot;:\&quot;1\&quot;,\&quot;device_status\&quot;:\&quot;0\&quot;}&quot;}]"
# def parseMessage(ws, message):
#     logUtil.renderConsole("on message %s" % message),
#     if message == "40":
#         logUtil.renderConsole("send 40 str"),
#         ws.send("40/ch_UwVEf0pG?token=ad133b75d9e54856a06f61d4a02df73f&ip=vhallim-connect05-online-ali-bje.vhouhn.com&port=8005&channelId=ch_UwVEf0pG&userId=113&appId=b7eb60bc&client=pc_browser&role=host&version=v3,")
#
#     if message == "40/ch_UwVEf0pG":
#         logUtil.renderConsole("send 40 channel"),
#         ws.send('42/ch_UwVEf0pG,["join",{"channel":"ch_UwVEf0pG","third_party_user_id":113,"context":"{\"nickname\":\"visitor_8179215\",\"avatar\":\"\",\"role_name\":2,\"device_type\":\"2\",\"device_status\":\"0\"}","hide":false}]')
#
#     if len(message) > 20:
#         logUtil.renderConsole("send 40 max length"),
#         ws.send('42/ch_UwVEf0pG,["join",{"channel":"ch_UwVEf0pG","third_party_user_id":113,"context":"{\"nickname\":\"visitor_8179215\",\"avatar\":\"\",\"role_name\":2,\"device_type\":\"2\",\"device_status\":\"0\"}","hide":false}]')
#
#     if message == "3":
#         logUtil.renderConsole("send 2")
#         ws.send("2")
#
#
# socketUtil.setOnMessage(lambda ws, message: (
#     parseMessage(ws, message)
# ))
# socketUtil.connect()
