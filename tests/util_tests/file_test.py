#!/usr/bin/env python
# encoding:utf8

import os
import sys
import require
from utils.cache_util import cacheUtil


cacheUtil.set("name", "nelsonking")
cacheUtil.set("go", "nelsonking")
cacheUtil.set("age", "18", 2)

print(cacheUtil.get("go"))
print(cacheUtil.get("name"))
print(cacheUtil.get("age"))


