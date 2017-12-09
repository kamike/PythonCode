#!/usr/bin/env python
#-*- coding:utf8 -*-
import os

import jpype
from jpype import *

imageUrl='http://pursuege.oss-cn-shenzhen.aliyuncs.com/img/timg.jpg'


# jar_path = os.path.join(os.path.abspath('.'), 'libs/AliyunOCR.jar')
jar_path = os.path.join(os.path.abspath('.'), 'libs/TestJava1_jar.jar')

print()
startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % jar_path)




com= jpype.JPackage('com.wangtao.python')
print(com)
TestStr=com.TestStr()
list=TestStr.getTestStr()

print(list)