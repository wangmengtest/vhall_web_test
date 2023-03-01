#!/usr/bin/env python
# encoding:utf8

"""
公共发送消息类，需要传入具体的实现方法
"""


class sendMessageUtil(object):
    driver = None

    def setDriver(self, driverApi):
        self.driver = driverApi

    def send(self, message):
        self.driver.send(message)
