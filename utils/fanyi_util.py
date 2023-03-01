#!/usr/bin/env python
# encoding:utf8

import require
from utils.request_util import requestUtil

class FanyiUtil(object):
    url= 'https://fanyi.baidu.com/sug'
    Form_data = {'kw': ""}

    def trans(self, query):
        # 最大取4字
        query = query[0:4]

        while True:
            menuList = self.collection(query)
            if not menuList:
                query = query[0:-1]

                if not query:
                    return ""
            else:
                return menuList        

    def collection(self, query):
        print(query)
        menuList = []
        self.Form_data['kw'] = query        
        response = requestUtil.post(self.url, self.Form_data)
        response = response.get("data")
        for i in response:
            singleMenu = i.get("v")
            singleMenuList = singleMenu.split(";")
            for singMenuInfo in singleMenuList:
                menuList.append(singMenuInfo)

        return menuList

fanyiUtil = FanyiUtil()
