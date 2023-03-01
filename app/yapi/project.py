#!/usr/bin/env python
# encoding:utf8

import require
from app.yapi.yapi_request import YapiRequest
from utils.request_util import requestUtil
from utils.random_util import randomUtil
from utils.fanyi_util import fanyiUtil


class Project(YapiRequest):
    def info(self, data):
        requestUtil.openDocHook("获取禅道信息")
        return self.get("/api/project/get", data)

    def add(self, data):
        requestUtil.openDocHook("添加项目")
        return self.post("/api/project/add", data)

    def addCat(self, data):
        requestUtil.openDocHook("添加菜单")    
        return self.post("/api/interface/add_cat", data)

    def delete(self, data):
        requestUtil.openDocHook("删除项目")
        return self.post("/api/project/del", data)

    def list(self, data):
        requestUtil.openDocHook("获取分组项目列表")
        return self.get("/api/project/list", data)

    def getMenu(self, data):
        requestUtil.openDocHook("获取分组菜单列表")
        return self.get("/api/interface/getCatMenu", data)

    def export(self, data):
        requestUtil.openDocHook("导出项目 json")
        return self.get("/api/plugin/export", data)

    def importJson(self, data):
        requestUtil.openDocHook("导入项目 json")
        return self.postJson("/api/interface/save", data)

    def icon(self, name):
        if name.find("统计") > -1:
            return "line-chart"

        if name.find("商品") > -1:
            return "qrcode"       

        iconList = ["retweet","shrink","arrow-salt","reload","minus-square-o","minus-circle","minus-circle-o","minus","plus-circle-o","plus-circle","plus","info-circle","info-circle-o","info","exclamation","exclamation-circle","exclamation-circle-o","close-circle","close-circle-o","check-circle","check-circle-o","check","close","credit-card","code-o","book","bars","question","question-circle","question-circle-o","pause","pause-circle","pause-circle-o","clock-circle","clock-circle-o","plus-square-o","frown-circle","copy","menu-fold","mail","logout","link","area-chart","line-chart","home","laptop","star","star-o","folder","filter","file","exception","meh-circle","meh-o","shopping-cart","save","user","video-camera","to-top","team","solution","search","share-alt","setting","poweroff","picture","phone","paper-clip","notification","mobile","inbox","lock","qrcode","play-circle","play-circle-o","tag","tag-o","tags","tags-o","cloud-o","cloud","cloud-upload","cloud-download","cloud-download-o","cloud-upload-o","environment","environment-o","eye","eye-o","camera","camera-o","aliwangwang","aliwangwang-o","export","edit","circle-down-o","circle-down-","appstore-o","appstore","scan","file-text","folder-open","hdd","ie","file-jpg","like","like-o","dislike","dislike-o","delete","enter","pushpin-o","pushpin","heart","heart-o","pay-circle","pay-circle-o","smile-circle","smile-o","frown-o","calculator","message","desktop","upload","download","pie-chart","unlock","calendar","windows-o","dot-chart","bar-chart","code","api","plus-square","minus-square","close-square","close-square-o","check-square","check-square-o","fast-backward","fast-forward","loading","loading-3-quarters","bulb","select","addfile","addfolder","switcher","rocket","dingding","dingding-o","bell","disconnect","database","compass","barcode","hourglass","key","flag","layout","login","printer","sound","usb","skin","tool","sync","wifi","car","copyright","schedule","user-add","user-delete","usergroup-add","usergroup-delete","man","woman","shop","gift","idcard","medicine-box","red-envelope","coffee","trademark","safety","wallet","bank","trophy","contacts","global","shake","fork","dashboard","profile","warning","slack","slack-square","dribbble","dribbble-square","instagram"]
        nameMeaningList = fanyiUtil.trans(name)

        for icon in iconList:
            for singMeaning in nameMeaningList:
                if singMeaning.find(icon) > -1:
                    return icon    

        for icon in iconList:
            for singMeaning in nameMeaningList:
                if icon.find(singMeaning) > -1:
                    return icon                     

        return randomUtil.choice(iconList)

    def color(self):
        # 红 黄 绿 蓝 紫 粉红色   
        colorList = ['red', 'yellow', 'green', 'blue', 'purple', 'pink']
        return randomUtil.choice(colorList)        


projectObj = Project()
