class Animal():
    def eat(self):
        print("----吃----")
    def drink(self):
        print("----喝------")
    def sleep(self):
        print("---睡觉----")
    def run(self):
        print("---跑----")
class Dog(Animal):  # 继承父类，在class（）中输入父类名， 就可以使用父类中的方法
    def bark(self):
        print("---汪汪叫-----")
class Cat(Animal):
    def catch(self):
        print("---抓老鼠----")

dog1 = Dog()
dog1.eat()
tom = Cat()
tom.drink()

"""
父类/基类<----子类/派生类

箭头方向表示后面的继承前面的
"""