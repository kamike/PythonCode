#!/usr/bin/env python
# -*- coding:utf8 -*-
import os
import configparser

conf = configparser.ConfigParser()
file=os.getcwd()+"/Config.conf";

conf.read(file)
session=conf.sections()
print("section",session)
print(conf.get("baidu","a"))



# imgUrl = "http://pursuege.oss-cn-shenzhen.aliyuncs.com/img/timg.jpg";
#
# client = AipOcr("10506105", "l6xFr9MFZrj1I6XkObWf7jqN", "3iDMlsadAXqy5CIOGIjW2pnr4KrHEey3 ")
#
# # 定义参数变量
# options = {
#     'detect_direction': 'true',
#     'language_type': 'CHN_ENG',
# }
# resoult = client.basicGeneral(imgUrl, options)
#
# print(resoult)
