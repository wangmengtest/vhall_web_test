#!/usr/bin/env python
# encoding:utf8

import configparser
import os
import sys
import require
from utils.log_util import logUtil


"""
公共配置类 单例
"""


class ConfigUtil(object):
    def __init__(self):
        self.configFile = require.configPath("/config.conf")
        self.config = configparser.ConfigParser()
        self.config.read(self.configFile)

    # 获取配置
    def get(self, section, option, default=None):
        try:
            return self.config.get(section, option)
        except Exception as e:
            logUtil.error(e)

        return default

    # 更新配置
    def set(self, section, option, value):
        self.config.set(section, option, value)

        with open(self.configFile, "w+") as handle:
            self.config.write(handle)


configUtil = ConfigUtil()
