#!/usr/bin/env python
# encoding:utf8

import ssl
import require
import websocket
import time
import json

"""
WebSocket接数据库类
"""

class WebSocketUtil(object):
    def __init__(self, url):
        self.url = url
        self.openListen = True
        self.socketObj = None
        self.onMessage = lambda ws, message: (
            print(message)
        )

    def connect(self):
        websocket.enableTrace(False)
        websocket.setdefaulttimeout(100000)

        self.socketObj = websocket.WebSocketApp(self.url,
                                                #on_open=self.onOpen(),
                                                on_message=self.getOnMessage(),
                                                on_data=self.getOnData(),
                                                on_error=self.getOnError(),
                                                on_close=self.getOnClose())
        #self.socketObj.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
        self.socketObj.on_open = self.onOpen()
        #self.socketObj.run_forever(ping_interval=5,ping_timeout=2)
        self.socketObj.run_forever()

    def setOnMessage(self, onMessageLambda):
        """
        set on message what to do
        :param onMessageLambda:
        :return:
        """
        self.onMessage = onMessageLambda

    def getOnMessage(self):
        """
        on message what to do
        :return:
        """
        return self.onMessage

    def getOnData(self):
        def run(ws, message, opcode, fin):
            self.onData(ws)

        return run

    def onData(self, ws):
        """
        on data and is not message what to do
        :param ws:
        :return:
        """
        return ws

    def onOpen(self):
        print("####### on_open #######")
        def run(*args):
            for i in range(10):
                #time.sleep(0.1)
                self.socketObj.send("40/ch_xqUad32b?token=f658fab3ab434a9680e3e814fbf7a466&ip=vhallim-connect02-online-ali-bje.vhouhn.com&port=8005&channelId=ch_xqUad32b&userId=52&appId=b6f14dbf&client=pc_browser&role=host&version=v3,")
                #time.sleep(1)
                #self.socketObj.send(json.dumps('42/ch_xqUad32b,["join",{"channel":"ch_xqUad32b","third_party_user_id":52,"context":"{"nickname":"mengmeng1","avatar":"","role_name":2,"device_type":"2","device_status":"0"}","hide":false}]'))
                #self.socketObj.send(json.dumps('42/ch_xqUad32b,["join",{"channel":"ch_xqUad32b","third_party_user_id":52,"context":"{"nickname":"mengmeng1","avatar":"","role_name":2,"device_type":"2","device_status":"0"}","hide":false}]'))
                self.socketObj.send('42["join",{channel:"ch_xqUad32b"},third_party_user_id:52,context:{\nickname\:\${nickname}\,\device_type\:\1\,\device_status\:\0\}}]')
                time.sleep(1)
                #self.socketObj.send(str(2))
            #time.sleep(1)
            #ws.close()
        return run

    def getOnError(self):
        func = lambda ws, error: (
            print(error),
            print("on error"),
        )

        return func

    def getOnClose(self):
        func = lambda ws, message, error: (
            print("on close"),
        )

        return func

    def close(self):
        if self.socketObj:
            self.socketObj.close()
