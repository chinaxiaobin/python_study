"""
├── infodisplay.py
└── Testmsg
    ├── __init__.py  #只要创建 了这个文件我们就称为Testmsg和里面的文件一起合称为包
    ├── __pycache__
    │   ├── __init__.cpython-35.pyc
    │   ├── recvmsg.cpython-35.pyc
    │   └── sendmsg.cpython-35.pyc
    ├── recvmsg.py
    └── sendmsg.py

"""
# vim infodisplay.py
def test3():
    print("--infodisplay--test3--")

# mkdir Testmsg
# mv recvmsg.py /Testmsg
# mv sendmsg.py /Testmsg
# vim recvmsg.py
def test2():
	print("---recvmsg-test2---")

# vim sendmsg.py
def test1():
	print("---sendmsg-test1---")

#vim __init__.py
__all__ = ["sendmsg"]

#<== __all__模块的作用是写上以后就可以使用 from Testmsg import *的时候这个语句会导入sendmsg
#然后 sendmsg.test1()就可以使用了

from . import recvmsg

#<==这个语句的意思是可以使用 Testmsg.recvmsg.test2()这个语句进行调用
