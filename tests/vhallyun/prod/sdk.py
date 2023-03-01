#!/usr/bin/env python
# encoding:utf8

import require
from hashlib import md5
from app.vhallyun.sdk import *
from utils.proxy_util import proxyUtil
from utils.config_util import configUtil
from utils.log_util import logUtil


testObj = Sdk("prod_pingan_vhallyun_api")

thirdPartUserId = "test_0720_001"
result = testObj.getAccessToken({
    "third_party_user_id": thirdPartUserId
})
accessToken = result.get('data').get("access_token")

iosBundleId = "com.pingan.PAMobileStockTrail.en,com.pingan.PAMobileStockTrail,com.pingan.PAMobileStockHigh,com.pingan.PAMobileStockHigh.en,com.pingan.PAMobileStockTrail,com.vhall.outsource.PinganHost.en"
iosPackList = [configUtil.get(testObj.section, "app_id"), iosBundleId]
iosPackStr = "|".join(iosPackList)
checkStr = md5(iosPackStr.encode('utf-8')).hexdigest()
checkStr = checkStr[0:16]

for i in range(200):
    requestUtil.setProxy(proxyUtil.getProxy())
    testObj.init({
        "client": "js",
        "third_party_user_id": thirdPartUserId,
        "access_token": accessToken,
        "package_check": checkStr,
    })
