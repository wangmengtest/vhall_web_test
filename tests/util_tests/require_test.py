#!/usr/bin/env python
# encoding:utf8

import os
import sys
import require
from utils.log_util import logUtil

# 指定跟目录 无require 时的一种临时解决方案
# rootName = "toolkit"
# currentPath = os.path.abspath(os.path.dirname(__file__))
# routPathSplit = currentPath.split(rootName)
# rootPath = routPathSplit[0] + rootName
# sys.path.append(rootPath)

import require
from utils.log_util import LogUtil

logUtil.render("hello")


