#!/usr/bin/env python
# -*- coding:utf8 -*-
import os
import configparser

from aip import AipOcr
import json
import re

# conf = configparser.ConfigParser()
# file=os.getcwd()+"/Config.conf";
#
# conf.read(file)
# session=conf.sections()
# print("section",session)
# print(conf.get("baidu","a"))



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



jsonStr="{'log_id': 1902239055352749612, 'direction': 0, 'words_result_num': 2, 'words_result': [{'words': '再不走'}, {'words': '就打死你'}]}"
jsonStr=re.sub("'","\"",jsonStr)
print(jsonStr)
resoult=json.loads(jsonStr)

print(resoult['log_id'])
print(resoult['direction'])
print(resoult['words_result_num'])
print(resoult['words_result'])
print(resoult['words_result'][0])
