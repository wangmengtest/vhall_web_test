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
创建 Laravel 实体
"""

template = """<?php
namespace Core\Entity{NameSpace};

use Entity\Input;
use Entity\SelectListTraits;
use Core\Models{NameSpace}\{Model};

class {Model}Entity extends Input
{
    use SelectListTraits;
    
{Attribute}

    // 模型字段验证，需要手动修改为合适结构
    public function validateModel(){
        $this->validateWithException([
{Check}        ]);
    }
    
    // 映射数据库字段
    public function mapDbFiled({Model} ${SmallModel})
    {
{MapDb}    }    
}
"""

dbUtil = DBUtil("dev_pingan_db")
params = sys.argv
if len(params) < 2:
    print("参数长度不正确")
    exit()
modelParam = params[1]

nameSpace = ""
nameSpacePath = ""
if len(params) > 2:
    nameSpaceParam = params[2]
    nameSpace = "\%s" % stringUtil.underLineToHump(nameSpaceParam, True)
    nameSpacePath = "/%s/" % stringUtil.underLineToHump(nameSpaceParam, True)


tableList = []
tables = dbUtil.select("SHOW TABLE STATUS WHERE	NAME LIKE %s", "%"+modelParam+"%")
for tableDict in tables:
    table = tableDict.get("Name")
    tableComment = tableDict.get("Comment")

    className = table.replace("qjy", "")
    className = re.sub("s$", "", className)
    className = stringUtil.underLineToHump(className)
    smallModel = table.replace("qjy_", "")
    smallModel = re.sub("s$", "", smallModel)
    smallModel = stringUtil.underLineToHump(smallModel)
    tableColumns = dbUtil.select("SHOW FULL COLUMNS FROM %s" % table)

    attribute = ""
    check = ""
    mapDb = ""

    for column in tableColumns:
        propField = column['Field']
        if propField in ["created_at", "updated_at", "deleted_at"]:
            continue

        columnType = column['Type']
        field = stringUtil.underLineToHump(propField)
        default = column['Default']
        comment = column['Comment']
        if comment:
            comment = re.sub("\r|\n", " ", comment)
            attribute += "    // %s \r" % comment

        if default and stringUtil.isNumber(default):
            attribute += "    public int $%s = 0;\r\r" % field
        else:
            attribute += "    public string $%s = \"\";\r\r" % field

        if propField != "id":
            check += "            '%s' => 'required',\r" % propField
            mapDb += "        $%s->%s = $this->%s;\r" % (smallModel, propField, field)

    tableList.append({
        'model': className,
        'smallModel': smallModel,
        'attribute': attribute,
        'check': check,
        'mapDb': mapDb,
    })

# 删除之前创建的文件
removePath = require.storagePath("/Entity/*.php")
os.system("rm -rf %s" % removePath)

for tableDict in tableList:
    newTemplate = template.replace("{Model}", tableDict.get("model"))
    newTemplate = newTemplate.replace("{NameSpace}", nameSpace)
    newTemplate = newTemplate.replace("{SmallModel}", tableDict.get("smallModel"))
    newTemplate = newTemplate.replace("{Attribute}", tableDict.get("attribute"))
    newTemplate = newTemplate.replace("{Check}", tableDict.get("check"))
    newTemplate = newTemplate.replace("{MapDb}", tableDict.get("mapDb"))

    fileObj = FileUtil(require.storagePath("/Entity/%sEntity.php" % tableDict.get("model")))
    print("add file %s" % require.storagePath("/Entity/%sEntity.php" % tableDict.get("model")))
    fileObj.append(newTemplate)
    fileObj.close()


packageDir = "/Users/nelsonking/Code/php/qjyedu-admin-api/Core"
targetEntityDir = "%s/Entity%s" % (packageDir, nameSpacePath)

os.system("mkdir -p %s" % targetEntityDir)

os.system("cp -rf /Users/nelsonking/Code/python/toolkit/storage/Entity/*.php %s" % targetEntityDir)




