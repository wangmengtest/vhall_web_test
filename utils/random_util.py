#!/usr/bin/env python
# encoding:utf8

import json
import require
import unicodedata
import prettyprinter
import random
import urllib
import requests
from utils.config_util import configUtil
from utils.request_util import requestUtil

"""
获取随机值 单例
"""


class RandomUtil(object):
    first_name = ["王", "李", "张", "刘", "赵", "蒋", "孟", "陈", "徐", "杨", "沈", "马", "高", "殷", "上官", "钟", "常"]
    second_name = ["伟", "华", "建国", "洋", "刚", "万里", "爱民", "牧", "陆", "路", "昕", "鑫", "兵", "硕", "志宏", "峰", "磊", "雷",
                   "文", "明浩", "光", "超", "军", "达"]

    en_first_name = ["yah", "aron", "arushi", "bagail", "bbey", "bbi", "bbie", "bby", "bdul",
                     "bdullah", "be", "bel", "bi", "bia", "bigail", "braham", "bram", "brianna",
                     "briel", "brielle", "by", "cacia", "ce", "da", "dalia", "dalyn", "dam", "dan", "ddie",
                     "ddison", "ddison", "de", "deide", "dele", "delene", "delia", "delina", "deline", "den", "dnan"]

    en_second_name = ["gie", "gnes", "hd", "hmed", "ida", "idan", "iden", "ileen", "ilsa",
                      "imee", "ine", "insleigh", "insley", "ley", "isha", "isling", "islinn",
                      "jay", "l", "lain", "danna", "drian", "driana", "drianna", "drianne",
                      "driel", "drienne", "erona", "gatha", "laina", "lan", "lana", "lanis", "lanna",
                      "lannah", "laska", "lastair", "layah", "layna", "lba", "lbert", "lberta",
                      "lberto", "lbie", "lden", "ldo", "leah", "lec", "lecia"]

    # 格式化输出 Json 对象
    def mobile(self, tag='cn'):
        if tag == "cn":
            return "1%s" % random.randint(1111111111, 9999999999)

        if tag == "en":
            return random.randint(1111111, 99999999999)

    def thirdPartyUserId(self, pointer=None):
        if pointer is not None:
            return pointer

        return random.randint(1111111111, 9999999999)

    def nickname(self, tag='cn'):
        if tag == "cn":
            return random.choice(self.first_name) + random.choice(self.second_name)
        if tag == "en":
            return random.choice(self.en_first_name) + random.choice(self.en_second_name)

    def avatar(self):
        randUrl = "https://picsum.photos/200/300"
        result = requests.get(randUrl)
        print(result)

    def localImg(self):
        return configUtil.get("env", "img_path") + "/background.png";

    def choice(self, customList):
        return random.choice(customList)


randomUtil = RandomUtil()
