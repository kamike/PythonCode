#!/usr/bin/env python
#-*- coding:utf8 -*-

from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot(cache_path=True)
bot.self.send('wo 是机器人')


# 进入 Python 命令行、让程序保持运行
# 推荐使用
embed()