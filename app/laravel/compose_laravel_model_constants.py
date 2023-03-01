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
namespace Core\Models{NameSpace};

use Core\Models\ModelInject;
use Illuminate\Database\Eloquent\Model;


/**
 * {COMMENT}
 * Class {Model}
 *
{Property}
 *
 * @package Core\Models{NameSpace}
 */
class {Model} extends Model
{
    use ModelInject;
    
    protected $table = "{TABLE}";

    public function __construct(array $attributes = [])
    {
        $this->fixFillAble();
        parent::__construct($attributes);
    }
}
"""

constantsTemplate = """<?php 
namespace Core\Constants{NameSpace};

/**
 * {Model} {FIELD} 静态变量
 * Class {CONSTANT}
 *
 * @package Core\Constants{NameSpace}
 */
class {CONSTANT}
{

{CONST}
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
tables = dbUtil.select("SHOW TABLE STATUS WHERE	NAME LIKE %s", "%" + modelParam + "%")
for tableDict in tables:
    table = tableDict.get("Name")
    tableComment = tableDict.get("Comment")

    className = table.replace("qjy", "")
    className = re.sub("s$", "", className)
    className = stringUtil.underLineToHump(className)

    tableColumns = dbUtil.select("SHOW FULL COLUMNS FROM %s" % table)

    prop = ""
    constList = []

    for column in tableColumns:
        field = column['Field']
        prop += " * @property $%s\r" % field
        comment = column['Comment']
        # 按数据量计算是否是枚举类型，进行静态数据划分
        commentValueMatch = re.compile("([a-z_A-Z\d]+)(?:\s+|$)").findall(comment)

        # 注释超过2个，进入枚举
        if len(commentValueMatch) >= 2:
            constList.append({field: comment})

    tableList.append({
        "model": className,
        "table": table,
        "prop": prop,
        "comment": tableComment,
        "const": constList
    })

# 构建模型 删除之前创建的文件
removePath = require.storagePath("/Model/*.php")
os.system("rm -rf %s" % removePath)

# 构建静态变量类 删除之前创建的文件
removeConstantsPath = require.storagePath("/Constants/*.php")
os.system("rm -rf %s" % removeConstantsPath)


def buildConst(model, constList):
    for commentDict in constList:
        for field in commentDict:
            constantClass = "%s%sConstants" % (model, stringUtil.underLineToHump(field, True))
            comment = commentDict[field]

            # 按数据量计算是否是枚举类型，进行静态数据划分
            commentValueMatch = re.compile("([a-z_A-Z\d]+)(?:\s+|$)").findall(comment)
            commentKeyMatch = re.compile("\S*[\u4e00-\u9fa5]+\S*").findall(comment)
            outIndex = len(commentKeyMatch) - len(commentValueMatch)

            const = ""
            if outIndex >= 1:
                firstComment = commentKeyMatch[0: outIndex]
                commentKeyMatch = commentKeyMatch[outIndex:]
                const = "    // %s\r\r" % " ".join(firstComment)
                const += "\r"

            print("build filed %s const" % field)

            for key, value in enumerate(commentValueMatch):
                comment = value
                constKey = value

                if len(commentKeyMatch) > key:
                    comment = commentKeyMatch[key]

                if len(commentValueMatch) == 2 and stringUtil.isNumber(value):
                    # 两位数字类型，不在添加惊天变量
                    print("fund number and skip")
                    continue

                if not stringUtil.isNumber(value):
                    value = '"%s"' % value

                const += "    // %s\r" % comment
                const += "    const %s = %s;\r" % (constKey, value)
                const += "\r"

            newConstTemplate = constantsTemplate.replace("{Model}", model)
            newConstTemplate = newConstTemplate.replace("{FIELD}", field)
            newConstTemplate = newConstTemplate.replace("{NameSpace}", nameSpace)
            newConstTemplate = newConstTemplate.replace("{CONSTANT}", constantClass)
            newConstTemplate = newConstTemplate.replace("{CONST}", const)

            constFileObj = FileUtil(require.storagePath("/Constants/%s.php" % constantClass))
            constFileObj.append(newConstTemplate)
            constFileObj.close()


for tableDict in tableList:
    modelName = tableDict.get("model") + "Model"
    newTemplate = template.replace("{Model}", modelName)
    newTemplate = newTemplate.replace("{NameSpace}", nameSpace)
    newTemplate = newTemplate.replace("{COMMENT}", tableDict.get("comment"))
    newTemplate = newTemplate.replace("{Property}", tableDict.get("prop"))
    newTemplate = newTemplate.replace("{TABLE}", tableDict.get("table").replace("qjy_", ""))

    fileObj = FileUtil(require.storagePath("/Model/%s.php" % modelName))
    fileObj.append(newTemplate)

    print("add file %s" % require.storagePath("/Model/%s.php" % tableDict.get("model")))

    constList = tableDict.get("const")
    if constList:
        buildConst(tableDict.get("model"), constList)
    fileObj.close()
