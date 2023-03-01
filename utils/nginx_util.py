#!/usr/bin/env python
# encoding:utf8

import os
import re
import require
import paramiko
from scp import SCPClient
from time import sleep

"""
nginx 操作类
"""


class NginxUtil(object):
    def __init__(self, sshUtil):
        self.sshUtil = sshUtil

    def dockerNginxReload(self):
        result = self.sshUtil.cmd("/usr/bin/docker exec -t nginx nginx -t")
        self._configCheck(result)

        self.sshUtil.cmd("/usr/bin/docker exec -t nginx nginx -s reload")
        print("重启 nginx 成功")

    def nginxReload(self):
        result = self.sshUtil.cmd("/usr/sbin/nginx -t")
        self._configCheck(result)

        self.sshUtil.cmd("/usr/sbin/nginx -s reload")
        print("重启 nginx 成功")

    def _execCmdCheck(self, error):
        """
        执行命令成功与否检测
        :param error:
        :return:
        """
        if error:
            print("命令执行失败")
            exit()

    def _configCheck(self, result):
        """
        nginx 配置文件检测
        :param result:
        :return:
        """
        if result.find("is success") == -1:
            result.find("is success")
            print(result)
            print("nginx 检测失败")
            exit()

    def _execReloadCheck(self, error):
        """
        重启 nginx 检测
        :param error:
        :return:
        """
        if error:
            print("重启 nginx 失败")
            exit()