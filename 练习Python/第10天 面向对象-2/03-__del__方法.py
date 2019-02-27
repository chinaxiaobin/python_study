class Dog():
    def __del__(self):
        print("======英雄挂了=====")

dog1 = Dog()
dog2 = dog1
del dog1  #<===不会调用 __del__方法,因为这个对象 还有其他的变量指向它,即 引用计数不是0
del dog2  #<===调用__del__方法，因为没有变量指向他了
print("llllllllllllllllllll")

#<程序结束后，如果还有其它对象还存在，那么python解释器会自动调用__del__来完成清除工作，如果之前调用了__del__，那么后
# 面程序结束后，就不再调用