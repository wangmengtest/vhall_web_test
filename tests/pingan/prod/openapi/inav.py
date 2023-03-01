#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.pingan.openapi.inav import *
from utils.config_util import configUtil
from utils.log_util import logUtil

testObj = Inav("prod_pingan_api")
testObj.setDbSection("dev_pingan_db")
testObj.setSignRequest()


ilId = 1100002359
accessData = testObj.getAccess({
    "il_id": ilId,
    'third_party_user_id': "test001"
})

accessToken = accessData.get("data").get("access_token")

roomInfoParam = {
    "il_id": ilId,
    "access_token": accessToken
}
testObj.getRoomInfo(roomInfoParam)

