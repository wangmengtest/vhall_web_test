#!.venv/bin/python
# encoding:utf8

import require
import cgi
import cgitb
cgitb.enable()
from app.preview.pingan.openapi.inav import *
from utils.random_util import randomUtil
from utils.cgi_util import cgiUtil

testObj = Inav("test_pingan_api")
testObj.setDbSection("dev_pingan_db")
testObj.setSignRequest()

form = cgi.FieldStorage()
ilId = form.getvalue('il_id')
env  = form.getvalue('env', 'prod')

if not ilId:
    cgiUtil.print("请传入 房间ID il_id")
    exit()

# 设置登录信息
testObj.setSignRequest()

params = testObj.postNoAppIdReturnRequestData({
    "thirdId": randomUtil.thirdPartyUserId(),
    "nickname": randomUtil.nickname(),
})

if env == "prod":
    env = "https://pingan.vhallyun.com"
else:
    env = "https://t-pingan.vhallyun.com"


address = "%s/fe-mobile/watch/%s?%s" % (env, ilId, params)
context = "接受参数如下 <br/>"
context += "il_id: 房间ID <br/>"
context += "env: prod 生产环境 <br/>"
context += "env: test 测试环境 <br/>"
context += "点击如下连接跳转至嵌入页面 <br/><br/>"
context += "<a href=%s>%s</a>" % (address, address)

cgiUtil.print(context)



