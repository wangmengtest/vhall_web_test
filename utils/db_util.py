#!/usr/bin/env python
# encoding:utf8

import pymysql
import require
from utils.config_util import configUtil

"""
公共数据库类
"""


class DBUtil(object):
    prefix = ""

    def __init__(self, section='local', host=None, port=None, user=None, password=None, database=None):
        if host and port and user and password and database:
            self.host = host
            self.port = port
            self.user = user
            self.password = password
            self.database = database
        else:
            self.host = configUtil.get(section, 'host')
            self.port = configUtil.get(section, 'port', 3306)
            self.user = configUtil.get(section, 'user')
            self.password = configUtil.get(section, 'password')
            self.database = configUtil.get(section, 'database')

        self.connection = pymysql.connect(
            host=self.host,
            port=int(self.port),
            user=self.user,
            password=self.password,
            db=self.database,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connection.cursor()

    # 表前缀
    def setPrefix(self, prefix):
        self.prefix = prefix

    # 查询类型支持
    # selectOne('select * from user where id = %s', 1)
    # selectOne('select * from user where id = 1 and type =1')
    # selectOne('select * from user where id = %s and type = %s', (1, 1))
    def selectOne(self, sql: object, band: object = ()) -> object:
        self.exec(sql, band)
        return self.cursor.fetchone()

    def select(self, sql, band=()):
        self.exec(sql, band)
        return self.cursor.fetchall()

    def update(self, sql, band=()):
        self.exec(sql, band)
        self.connection.commit()

    def insert(self, sql, band=()):
        self.exec(sql, band)
        self.connection.commit()

    def delete(self, sql, band=()):
        self.exec(sql, band)
        self.connection.commit()

    def escapeString(self, string):
        return self.connection.escape_string(str(string))

    def exec(self, sql, band):
        return self.cursor.execute(sql, band)

    # 获取组装的字典合成Sql查询字串
    # expect 取值为 key,value
    # key 追加 ``
    # value 根据类型追加 单引号
    def getDictPackageStr(self, data, originSymbolChar, originLinkChar, expect=None):
        symbolChar = self.composeStrFormat(originSymbolChar)
        linkChar = self.composeStrFormat(originLinkChar)
        sqlStr = ""

        for key in data:
            # 整形 None In 查询 不加工数据
            if isinstance(data[key], int) \
                    or data[key] is None \
                    or originSymbolChar == "in":

                value = data[key]
            else:
                value = self.escapeString(data[key])

            # 只保留 KEY
            if expect == "key":
                sqlStr += "`%s`%s" % (key, linkChar)

            # 只保留值
            elif expect == "value":
                if isinstance(value, int):
                    sqlStr += "%s%s" % (value, linkChar)
                elif value is None:
                    sqlStr += "Null%s" % linkChar
                else:
                    sqlStr += '"%s"%s' % (value, linkChar)
            else:
                if isinstance(value, int):
                    sqlStr += "`%s`%s%s%s" % (key, symbolChar, value, linkChar)
                elif originSymbolChar == "in":
                    sqlStr += "`%s`%s%s%s" % (key, symbolChar, value, linkChar)
                else:
                    sqlStr += '`%s`%s"%s"%s' % (key, symbolChar, value, linkChar)

        linkCharLen = 0 - len(linkChar)
        sqlStr = sqlStr[0:linkCharLen]

        return sqlStr

    # 获取格式化的分隔符
    def composeStrFormat(self, sqlStr):
        if sqlStr[0:1] != " ":
            sqlStr = " " + sqlStr

        if sqlStr[-1:] != " ":
            sqlStr += " "
        return sqlStr

    # 获取 where 的表达式 符号 和 连接符
    def composeWhereData(self, where):
        symbol = "="
        link = "and"

        if "symbol" in where:
            symbol = where["symbol"]
            del where["symbol"]

        if "link" in where:
            link = where["link"]
            del where["link"]

        return where, symbol, link

    #  组装插入语句
    def composeInsert(self, table, data):
        indexData = self.getDictPackageStr(data, "", ",", "key")
        valueData = self.getDictPackageStr(data, "", ",", "value")

        sql = "INSERT INTO %s (%s) VALUES (%s);" % (self.getTable(table), indexData, valueData)
        return self.composeSqlLast(sql)

    #  组装删除语句
    def composeDelete(self, table, where):
        where, symbol, link = self.composeWhereData(where)
        whereData = self.getDictPackageStr(where, symbol, link)

        sql = "delete from %s where %s;" % (self.getTable(table), whereData)
        return self.composeSqlLast(sql)

    #  组装更新语句
    def composeUpdate(self, table, update, where):
        where, symbol, link = self.composeWhereData(where)
        whereData = self.getDictPackageStr(where, symbol, link)

        updateData = self.getDictPackageStr(update, "=", ",")

        sql = "update %s set %s where %s;" % (self.getTable(table), updateData, whereData)
        return self.composeSqlLast(sql)

    #  组装查询语句
    def composeSelect(self, table, where, column='*'):
        if where:
            where, symbol, link = self.composeWhereData(where)
            whereData = self.getDictPackageStr(where, symbol, link)
            sql = "select %s from %s where %s;" % (column, table, whereData)
        else:
            sql = "select %s from %s;" % (column, self.getTable(table))
        return self.composeSqlLast(sql)

    # 生成Sql 最后处理
    def composeSqlLast(self, sql):
        # 单个元祖数据导致多一个逗号问题
        sql = sql.replace(",)", ")")

        return sql

    def composeInsertExec(self, table, data):
        sql = self.composeInsert(table, data)
        self.insert(sql)

    def composeDeleteExec(self, table, where):
        sql = self.composeDelete(table, where)
        return self.delete(sql)

    def composeUpdateExec(self, table, update, where):
        sql = self.composeUpdate(table, update, where)
        return self.update(sql)

    def composeSelectOneExec(self, table, where, column='*'):
        sql = self.composeSelect(table, where, column)
        return self.selectOne(sql)

    def composeSelectExec(self, table, where, column='*'):
        sql = self.composeSelect(table, where, column)
        return self.select(sql)

    def getTable(self, table):
        return self.prefix + table

    def close(self):
        self.cursor.close()
        self.connection.close()
