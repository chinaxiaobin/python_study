#  mkdir  file1
#  vi sendmsg.py
def test1():
    print("--test1---")

# vi revmsg.py
def test1():
    print("--")
# vi main.py
import sendmsg  #不要写后缀.py   默认搜索本地的，本地没有搜索系统的
import revmsg
sendmsg.test1()
revmsg.test1()

# python3 main.py 执行
"""
# tree
-- main.py
-- __pycache__  #缓存python解释的代码
   sendmsg.cpython-35.pyc  #字节码
            # 表示只能用c语言写的python解释器的第3.5个版本才能用
-- sendmsg.py

"""

###第二种方法
#vi main.py
from sendmsg import test1
from revmsg import test1
# from sendmsg import test1,test2  #导入多个函数，注意导入一个模块的时候就是从头到尾执行一遍
# from sendmsg import *  #尽量少用*，如果有多个py文件有相同的函数的时候，后面导入会顶替前面的
test1()

##################给模块起别名
import time as tt
tt.sleep(3)

############################
"""
因为每个人负责的代码不一样，所以自己写完要测试一遍，然后再一起测试，但是测试代码不能写了删除
删除了再写很麻烦

我们可以这样
"""

def test1():
    print("---test1---")
def test2():
    print("---test2---")

if __name__ == "__main__":
    test1()
    test2()

"""
print(__name__) 当 __name__我们自己执行的时候会显示__main__
当使用main.py调用的时候__name__会显示我们代码的名字，上面就是用的这么个道理
"""