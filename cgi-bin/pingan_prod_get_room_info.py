#!.venv/bin/python
# encoding:utf8

import require
import cgi
import cgitb
cgitb.enable()
from app.preview.pingan.openapi.inav import *
from utils.cgi_util import cgiUtil

testObj = Inav("prod_pingan_api")
testObj.setDbSection("dev_pingan_db")
testObj.setSignRequest()

form = cgi.FieldStorage()
ilId = form.getvalue('il_id')
json = form.getvalue('json')

if not ilId:
    cgiUtil.printJson()
    cgiUtil.print("请传入 房间ID il_id")
    exit()

accessData = testObj.getAccess({
    "il_id": ilId,
    'third_party_user_id': "test001",
    'watch_incr': 1,
})

if not accessData:
    cgiUtil.print("accessToken 获取失败 %s" % accessData)
    exit()

accessToken = accessData.get("data").get("access_token")

roomInfoParam = {
    "il_id": ilId,
    "access_token": accessToken
}
result = testObj.getRoomInfo(roomInfoParam)

if json:
    cgiUtil.printJson()
    print(result)
else:
    cgiUtil.printLog()


