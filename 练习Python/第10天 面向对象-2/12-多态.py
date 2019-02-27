class Dog():
    def print_self(self):
        print("大家好，我是xxxx,希望以后大家多多关照....")
class Xiaotq():
    def print_self(self):
        print("hello everybody,我是你们的老大，我是xxxx")

def introduce(temp)
    temp.print_self()

dog1 = Dog()
dog2 = Xiaotq()

introduce(dog1)
introduce(dog2)

#多态就是  你向函数传递不同的参数，会调取不同的方法，返回不同的结果

#python既支持面向过程编程也支持面向对象编程
#面向对象三要素
#封装：把函数和全局变量又封装起来，称为对象，这就是封装
#继承：子类集成父类的功能
#多态：定义的时候不确定调用哪个功能，而等到真正调用的时候才确定调用父类还是子类的功能