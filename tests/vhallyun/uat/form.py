#!/usr/bin/env python
# encoding:utf8
import require
from app.vhallyun.form import *
import json

testObj = Form("uat_herbalife_vhalyun_api")

answerCreate = {
    "id": "580684",
    "client": "pc_browser",
    "answer": json.dumps({
        1: "A",
        2: 'B',
        3: "C"
    })
}

testObj.answerCreate(answerCreate)