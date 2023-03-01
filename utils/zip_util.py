#!/usr/bin/env python
# encoding:utf8

import os
import require
import zipfile
import os.path
import platform
import threading


def isWindowsSystem():
    return 'Windows' in platform.system()


def isLinuxSystem():
    return 'Linux' in platform.system()


"""
zip文件压缩 类
"""


class ZipUtil(object):

    def zip_file(self, fs_name, fz_name):
        """
        从压缩文件
        :param fs_name: 源文件名
        :param fz_name: 压缩后文件名
        :return:
        """
        flag = False
        if fs_name and fz_name:
            try:
                with zipfile.ZipFile(fz_name, mode='w', compression=zipfile.ZIP_DEFLATED) as zipf:
                    zipf.write(fs_name)
                    print("%s is running [%s] " % (threading.currentThread().getName(), fs_name))
                    print('压缩文件[{}]成功'.format(fs_name))
                if zipfile.is_zipfile(fz_name):
                    os.remove(fs_name)
                    print('删除文件[{}]成功'.format(fs_name))
                flag = True
            except Exception as e:
                print('压缩文件[{}]失败'.format(fs_name), str(e))

        else:
            print('文件名不能为空')
        return {'file_name': fs_name, 'flag': flag}

    def unzip_file(self, fz_name, path, members=None, pwd=None):
        """
        解压缩文件
        :param fz_name: zip文件
        :param path: 解压缩路径
        :param members: 解压成员列表
        :param pwd: 解压密码
        :return:
        """
        flag = False
        print("解压文件 %s ing" % fz_name)

        if zipfile.is_zipfile(fz_name):  # 检查是否为zip文件
            with zipfile.ZipFile(fz_name, 'r') as zipf:
                zipf.extractall(path, members, pwd)
                if isWindowsSystem():
                    for p in zipf.namelist():
                        # 使用cp437对文件名进行解码还原， win下一般使用的是gbk编码
                        p = p.encode('cp437').decode('gbk')  # 解决中文乱码
                        print(fz_name, p, path)
                flag = True

        return {'file_name': fz_name, 'flag': flag}

    def unzip_list(self, fz_name, filter_size=0):
        """
        查看压缩文件，返回字段{文件名:大小}
        :param fz_name:
        :param filter_size 过滤大小 接受KB 为 单位
        :return:
        """
        result = {}
        if not zipfile.is_zipfile(fz_name):
            return result

        filter_size = filter_size * 1024
        with zipfile.ZipFile(fz_name, 'r') as zipf:
            infoList = zipf.infolist()
            for i in infoList:
                # 隐藏文件过滤
                if i.filename.find(".DS_Store") > -1:
                    continue

                if i.file_size > filter_size:
                    result[i.filename] = i.file_size

        return result


zipUtil = ZipUtil()
