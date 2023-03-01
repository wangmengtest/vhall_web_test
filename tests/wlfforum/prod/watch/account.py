#!/usr/bin/env python
# encoding:utf8
import require
from app.preview.wlaforum.watch.account import *
from utils.config_util import configUtil
from utils.random_util import randomUtil

testObj = Account("prod_wlaforum_api")
testObj.setDbSection("dev_wlaforum_db")

# 【必选】`user_id`      --》用户ID
# 【必选】`username`    --》用户名
# 【必选】`agenda_id`     --》议程ID
# 【必选】`account_type` --》用户类型1—嘉宾；2—观看用户
# 【可选】edition       --》中英文标识（zh 中文、en 英文）

currentEdition = "zh"
currentRoom = 72
reverseRoom = 60

userId   = randomUtil.thirdPartyUserId(5854667046)
roleType = 2

if userId == 0:
    roleType = 2

createMasterToken = {
    "user_id": userId,
    "username": "陈达",
    "nick_name": "马硕",
    "agenda_id": 1,
    "account_type": roleType,
    "edition": currentEdition,
    "room_id": reverseRoom,
}
print(createMasterToken)

result = testObj.createMasterToken(createMasterToken)

if roleType == 1:
    watchUrl = "%s/live-room/watch/%s?roleType=guest&token=%s" % (testObj.getFrontDomain(), currentRoom, result.get("data"))
else:
    watchUrl = "%s/live-room/watch/%s?token=%s" % (testObj.getFrontDomain(), currentRoom, result.get("data"))
print(watchUrl)
