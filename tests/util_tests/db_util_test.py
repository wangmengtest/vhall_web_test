#!/usr/bin/env python
# encoding:utf8

import os
import sys
import require
from utils.db_util import DBUtil
from utils.file_util import FileUtil

fileUtil = FileUtil(require.rootPath("/sql/db_util_test.sql"))

dbUtil = DBUtil("local")

insertSql = dbUtil.composeInsert("qjy_class_users", {"class_id": 666, "user_id": user_id, "book_id": 666})
fileUtil.append(insertSql)

editSql = dbUtil.composeUpdate("qjy_class_users", {"class_id": 777, "user_id": 777}, {"class_id": 666, "user_id": 666})
fileUtil.append(editSql)

selectSql = dbUtil.composeSelect("qjy_class_users", {"class_id": 777, "user_id": user_id})
fileUtil.append(selectSql)

deleteSql = dbUtil.composeDelete("qjy_class_users", {"class_id": 777, "user_id": 777, "book_id": 666})
fileUtil.append(deleteSql)

