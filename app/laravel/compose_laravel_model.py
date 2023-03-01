#!/usr/bin/env python
# encoding:utf8


import os
import sys
import re
import require

from utils.db_util import DBUtil
from utils.file_util import FileUtil
from utils.list_util import listUtil
from utils.string_util import stringUtil

"""
创建 Laravel 模型
"""

template = """<?php 

namespace web\models;

use web\common\WebBaseModel;

/**
 * {COMMENT}
 * Class {Model}
 *
{Property}
 *
 * @package Core\Models
 */

class {Model} extends WebBaseModel
{
    protected $table = "{TABLE}";

{CONST}

}
"""


dbUtil = DBUtil("dev_pingan_db")
params = sys.argv
if len(params) != 2:
    print("参数长度不正确")
    exit()
modelParam = params[1]

tableList = []
tables = dbUtil.select("SHOW TABLE STATUS WHERE	NAME LIKE %s", "%"+modelParam+"%")
for tableDict in tables:
    table = tableDict.get("Name")
    tableComment = tableDict.get("Comment")

    className = table.replace("qjy", "")
    className = re.sub("s$", "", className)
    className = stringUtil.underLineToHump(className, True)

    tableColumns = dbUtil.select("SHOW FULL COLUMNS FROM %s" % table)

    const = ""
    prop = ""

    for column in tableColumns:
        field = column['Field']
        prop += " * @property $%s\r" % field
        comment = column['Comment']
        # 按数据量计算是否是枚举类型，进行静态数据划分
        commentValueMatch = re.compile("([a-z_A-Z\d]+)(?:\s+|$)").findall(comment)
        commentKeyMatch = re.compile("\S*[\u4e00-\u9fa5]+\S*").findall(comment)

        # 注释超过2个，进入枚举
        if len(commentValueMatch) >= 2:
            outIndex = len(commentKeyMatch) - len(commentValueMatch)
            if outIndex >= 1:
                firstComment = commentKeyMatch[0: outIndex]
                commentKeyMatch = commentKeyMatch[outIndex:]
                const += "    // %s\r\r" % " ".join(firstComment)

            for key, value in enumerate(commentValueMatch):
                comment = value
                constKey = value
                if len(commentKeyMatch) > key:
                    comment = commentKeyMatch[key]

                if len(commentValueMatch) == 2 and stringUtil.isNumber(value):
                    if stringUtil.toNumber(value) == 1:
                        constKey = "TRUE"
                    if stringUtil.toNumber(value) == 2:
                        constKey = "FALSE"

                if not stringUtil.isNumber(value):
                    value = '"%s"' % value

                const += "    // %s\r" % comment
                const += "    const %s_%s = %s;\r" % (str(field).upper(), constKey, value)
            const += "\r"

    tableList.append({
        "model": className,
        "table": table,
        "const": const,
        "prop": prop,
        "comment": tableComment
    })

# 删除之前创建的文件
removePath = require.storagePath("/Model/*.php")
os.system("rm -rf %s" % removePath)

for tableDict in tableList:
    newTemplate = template.replace("{Model}", tableDict.get("model"))
    newTemplate = newTemplate.replace("{COMMENT}", tableDict.get("comment"))
    newTemplate = newTemplate.replace("{Property}", tableDict.get("prop"))
    newTemplate = newTemplate.replace("{TABLE}", tableDict.get("table").replace("qjy_", ""))
    newTemplate = newTemplate.replace("{CONST}", tableDict.get("const"))

    fileObj = FileUtil(require.storagePath("/Model/%s.php" % tableDict.get("model")))
    fileObj.append(newTemplate)

    print("add file %s" % require.storagePath("/Model/%s.php" % tableDict.get("model")))






