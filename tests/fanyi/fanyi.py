#!/usr/bin/env python
# encoding:utf8

import json
import os
import sys
import require
from utils.fanyi_util import fanyiUtil

entry = "邀请卡"
result = fanyiUtil.trans(entry)
print(result)
