#!/usr/bin/env python
# encoding:utf8

import json
import require
import time
from utils.file_util import FileUtil

"""
缓存类 JSON 类型缓存 单例
"""


class CacheUtil(object):
    cacheFileWrite = None

    def __init__(self):
        # 缓存句柄
        self.cacheFile = require.cachePath("/cache.json")
        self.cacheFileRead = FileUtil(self.cacheFile, 'r')
        content = self.cacheFileRead.read()

        if content:
            self.cacheData = json.loads(content)
        else:
            self.cacheData = {}

        self.unixTime = int(time.time())

    # 新增配置
    def set(self, key, value, ttl=3600*24):
        if self.cacheFileWrite:
            self.cacheFileWrite.close()

        # 重新写入文件
        self.cacheFileWrite = FileUtil(self.cacheFile, 'w')

        self.cacheData[key] = {
            "key": value,
            "ttl":  self.unixTime + ttl
        }

        self.cacheFileWrite.writeFirstLine(json.dumps(self.cacheData, ensure_ascii=False))

    # 读取配置
    def get(self, key, default=False):
        if key in self.cacheData:
            cacheData = self.cacheData[key]
            if "ttl" in cacheData and "key" in cacheData:
                # 缓存时间剩余超过2秒才才认为存在
                if cacheData["ttl"] - self.unixTime > 2:
                    return cacheData['key']
                else:
                    # 否则数据直接过期处理
                    self.set(key, {})

        return default


cacheUtil = CacheUtil()
