# 需要在ipython3中联系，创建 msgnew模块
__all__ = ["test1","Test","name"]
def test1():
	print("-----Test-----")
def test2():
	print("-----Test2-----")

name = 100
class Test(object):
	print("test lei")


"""
需要在ipython3中练习
有的时候 from msgnew import * 有些方法可能重名我们不希望被调用
__all__ = ["test1","Test"] 意思是当我们 from msgnew import * 的时候只会
导入我们这里指定的功能，直接输入test1()就可以显示， 直接输入test2就不行
t = Test()也可以直接创建对象
"""