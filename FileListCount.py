#!/usr/bin/env python
# -*- coding:utf8 -*-
import os

# 统计有多少行有效代码，除去空格大括号

global total_count
global space_count

total_count = 0
space_count = 0

# 文件路径后面必须带\\
fileDir = "G:\\python_data\\my_test\\giiiplus\\utils\\";


def forFirle(prentDir):
    global total_count
    dir = os.listdir(prentDir)
    for path in dir:
        filePath = prentDir + path;
        if os.path.isfile(filePath):
            count = 0;
            with open(filePath, 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    if isRealyCode(line):
                        count += 1
            total_count += count;
            print("文件：" + filePath + "      " + str(count))

        else:
            forFirle(filePath + "\\")


def isRealyCode(lineStr):
    if lineStr.isspace() or lineStr == "{" or lineStr == "}" or lineStr.startswith("import "):
        global space_count
        space_count += 1
        return False
    return True


forFirle(fileDir)
print("最终多少行有效代码：" + str(total_count) + ",有多少空格或{}：" + str(space_count) + ",总计：" + str(total_count + space_count))
input()
V