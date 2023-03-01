#!/usr/bin/env python
# encoding:utf8

import os
import sys
import require
from utils.db_util import DBUtil
from utils.file_util import FileUtil
from utils.log_util import logUtil

dbUtil = DBUtil("prod")
result = dbUtil.select("select * from qjy_memory_tools where id < 10")

logUtil.render(result)


