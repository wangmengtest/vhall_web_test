#!/usr/bin/env python
# encoding:utf8
import require
from app.upload.csces import *
from utils.random_util import randomUtil
from utils.config_util import configUtil

testObj = Csces("csces_uopload")

upload = {
    'path': 'img',
}
testObj.doUpload(randomUtil.localImg(), upload)




