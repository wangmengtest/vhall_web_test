#!/usr/bin/env python
# encoding:utf8

import os
import sys
import require
from utils.file_util import FileUtil
from utils.web_socket_util import WebSocketUtil
from utils.request_util import requestUtil


fileUtil = FileUtil(require.logPath("/log.txt"))

url = "wss://chat01.e.vhall.com/ws/ch_xqUad32b?date=1627288436524&_=1627288436524&tag=&time=&eventid="
# url = "wss://msg01-open.e.vhall.com/socket.io/?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1eF90aW1lIjoxNjI0ODY5NjkwNzEzLCJpcCI6IjEuMTE5LjE5My4zNiIsImNsaWVudCI6InBjX2Jyb3dzZXIiLCJhcHBfaWQiOiI2MTQ3Yjk0YSIsInBsYXRmb3JtIjoidm9wIiwidGltZXN0YW1wIjoxNjI0ODY5NjkwfQ.u3CciPp0Sz9kxLIW86BTHsa46b6a_GCLffdcBJw4XaQ&EIO=3&transport=websocket"

# socketUtil = WebSocketUtil("wss://msg01-open.e.vhall.com/socket.io/?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBfaWQiOiI2MTQ3Yjk0YSIsImNsaWVudCI6InBjX2Jyb3dzZXIiLCJwbGF0Zm9ybSI6InZvcCIsInRpbWVzdGFtcCI6MTYyMzI5MzkwOCwiaXAiOiIxLjExOS4xOTMuMzYiLCJ1eF90aW1lIjoxNjIzMjkzOTA4MTQzfQ.KWcZ9QmRCwA17FbctLgOmoYG7cGMf-aYqJahk5YMImc&EIO=3&transport=websocket")
#url = "wss://im-connect.vhall.com/socket.io/?token=f658fab3ab434a9680e3e814fbf7a466&ip=vhallim-connect11-online-ali-bje.vhouhn.com&port=8005&channelId=ch_xqUad32b&userId=3505&appId=b6f14dbf&client=pc_browser&role=host&version=v3&EIO=3&transport=websocket"
socketUtil = WebSocketUtil(url)
socketUtil.connect()




