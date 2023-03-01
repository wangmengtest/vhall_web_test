#!/usr/bin/env python
# encoding:utf8

import require
from app.upload.upload_request import UploadRequest
from utils.request_util import requestUtil

class Csces(UploadRequest):
    def doUpload(self, path, data):
        requestUtil.openDocHook("上传", self.dbUtil)
        return self.upload("files/upload",'file', path, data)
