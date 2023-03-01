#!/usr/bin/env python
# encoding:utf8

import numpy

from utils.db_util import DBUtil
from api.qjy.qjy_lib import QjyLib

dbUtil = DBUtil("local")
qjyLib = QjyLib(dbUtil)


result = numpy.linspace(1, 50)

for i in numpy.linspace(2, 50):
    print(i)
