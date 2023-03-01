#!/usr/bin/env python
# encoding:utf8

import os
import sys
import require
from utils.cache_util import cacheUtil
from utils.ssh_util import SShUtil

# sshUtil = SShUtil('47.106.203.84', 'root', '/Users/nelsonking/home/bash/id_rsa')
sshUtil = SShUtil('192.168.10.234', 'root', '/Users/nelsonking/home/bash/id_rsa')
# sshUtil.scp("/Users/nelsonking/home/bash/qjy/ssh/qjy_id_rsa", '/data')

# result = sshUtil.cmd("/usr/sbin/nginx -s reload")
# result = sshUtil.cmd("ls /")
result = sshUtil.cmd("/usr/bin/docker exec -t nginx nginx -t")
print(result)
exit()

if not result.find("is success") > -1:
    print("nginx 检测失败")
    exit()
#
#
# result = sshUtil.cmd("/usr/bin/docker exec -t nginx nginx -s reload")

#     print(result)
#     print("重启 nginx 成功")
