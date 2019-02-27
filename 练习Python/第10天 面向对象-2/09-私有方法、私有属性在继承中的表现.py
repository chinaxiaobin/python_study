
class A():
    def __init__(self):
        self.number = 100
        self.__number2 = 200

    def test1(self):
        print("----test1----")

    def __test2(self):
        print("----test2----")

    def test3(self):
        self.__test2()
        print(self.__number2)
class B(A):
    def test4(self):
        self.__test2()
        print(self.__number2)

b = B()
print(b.number)
#print(b.__nmuber2)   #私有属性不能被继承
b.test1()
#b.__test2() #私有方法不能被继承
#b.test3()   #如果调用的是继承的父类中的共有方法，可以在这个公有方法中访问父类中的私有属性和私有方法
#b.test4()
#但是如果在子类中实现了一个公有方法，那么这个方法是不能够调用继承父类中的私有方法
