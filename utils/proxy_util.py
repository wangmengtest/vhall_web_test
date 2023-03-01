#!/usr/bin/env python
# encoding:utf8

import require
from utils.time_util import timeUtil
from utils.request_util import requestUtil

"""
代理请求请求类 单例
使用熊猫代理工具
http://www.xiongmaodaili.com/usercenter/order
"""


class ProxyUtil(object):
    ipList = []
    ipListTime = None

    def getIpList(self):
        # 使用时替换为供应商提供的获取IP接口
        getIpListAddr = "http://route.xiongmaodaili.com/xiongmao-web/api/glip?secret=0a553982370963fd8e40ef7680b5be52&orderNo=GL20210720155659QP2OIvBM&count=10&isTxt=0&proxyType=1"
        result = requestUtil.get(getIpListAddr)
        self.ipList = result.get("obj")
        self.ipListTime = timeUtil.getTimeIntSecond()

    def getProxy(self):
        if self.ipList:
            ipAddress = list.pop(self.ipList)
        else:
            if timeUtil.getTimeIntSecond() == self.ipListTime:
                print("请求过快，接口跟不上了，休息一秒")
                timeUtil.sleep(1)

            self.getIpList()
            ipAddress = list.pop(self.ipList)

        ip = ipAddress.get("ip")
        port = ipAddress.get("port")
        ip_port = ip + ":" + port

        return {"https": "http://" + ip_port, "http": "http://" + ip_port}


proxyUtil = ProxyUtil()
