#!/usr/bin/env python
# -*- coding:utf8 -*-
from FileBean import FileBean
from OcrBean import OcrBean
from SQLUtils import SQLUtils
import hashlib

utils = SQLUtils()
fileBean = FileBean("http://baiodu.com","fileName",'a/dwaw','100',"md5111",'100','300',"baidu")
utils.addTableFile(fileBean)
orc=OcrBean("表情文字",0,"关键字","baidu","baidu.com")
utils.addTableOcr(orc)
utils.closedAll()
# md5file=open("G:/python_data/my_test/111/a.txt",'rb')
# md5=hashlib.md5(md5file.read()).hexdigest()
# print(md5)
