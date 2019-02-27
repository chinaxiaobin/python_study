"""
import os
os.__file__ #显示python解释器模块的路径，

import Testmsg #默认去当前路径找这个模块，没有就去上面的python解释器模块的路径查找

"""
# mkdir 03-模块发布
# cp -r 02-包/Testmsg   03-模块发布
#vim setup.py  #和Testmsg一个目录下，然后添加以下内容
from distutils.core import setup

setup(name="dongGe", version="1.0", description="dongGe's module", author="dongGe", py_modules=['Testmsg.sendmsg','Testmsg.recvmsg' ])

#构建模块
python3  setup.py  building

#生成压缩包
python3  setup.py  sdist

#安装
找到模块的压缩包
解压
进入文件夹
执行命令python3 setup.py install