#!/usr/bin/env python
# encoding:utf8

import os
import sys
import require
from utils.file_util import FileUtil

sourceStr = """卫材,PaaS定制项目,,,使用问题,,,会议时常9.52-10.24分这段时间的直播间处理断流状态，直播间状态为直播中，用户进入直播间是无法拉流的，所以用户看到直播画面属于正常情况，同时播放器也无法上报数据，参会数据也就对不上了。,测试,直播中,,,使用问题"""
sourceStrArray = sourceStr.split(",")
targetArray = sourceStrArray[7:10]

targetStr = ",".join(targetArray)
print(sourceStrArray)
print(targetArray)
print(targetStr)



