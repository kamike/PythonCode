#!/usr/bin/env python
# -*- coding:utf8 -*-
from urllib import request
from bs4 import BeautifulSoup
import time
import re

chartSet = 'utf-8';

url ='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word=%E8%A1%A8%E6%83%85'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

page = request.Request(url, headers=headers)
page_info = request.urlopen(page).read().decode(chartSet)

with open("G:\\python_data\\data\\data.html", "w+", encoding=chartSet) as file:
    file.write(page_info)

# 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
soup = BeautifulSoup(page_info, 'html.parser')
links = soup.find_all('img')
local_path = "G:\\python_data\\imgs\\";

for link in links:

    print("图片地址:" + link.attrs['src'])
    request.urlretrieve("http:"+link.attrs['src'], (local_path +str(time.time())+".jpg"))

print("end============")
file.close()
