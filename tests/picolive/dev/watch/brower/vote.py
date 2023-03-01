#!/usr/bin/env python
# encoding:utf8

from app.preview.picolive.watch.vote import *
from utils.config_util import configUtil

testObj = Vote("dev_picolive_api")
testObj.setDbSection("dev_picolive_db")

# 设置登录信息
token = configUtil.get(testObj.section, "admin_token")
testObj.setCommonData({'token': token})
testObj.setSignRequest()


voteAnswerParams = {
    'room_id': 'lss_f47a3e30',
    'extend': '{}',
    'vote_id': '559863',
    'answer_id': '947769',
}
testObj.voteAnswer(voteAnswerParams)