class Animal():
    def eat(self):
        print("----吃----")
    def drink(self):
        print("----喝----")
    def sleep(self):
        print("----睡觉----")
    def run(self):
        print("----跑----")

class Dog(Animal):
    def bark(self):
        print("---汪汪叫----")
class Xiaotq(Dog):
    def fly(self):
        print("----飞-----")
    def bark(self):
        print("-----狂叫-----")

#<===当父类的方法不满足需要时，又想调用这个方法名，可以自己创建相同的方法
#默认调用自己的方法，这就是重写

xiaotq = Xiaotq()
xiaotq.fly()
xiaotq.bark()
xiaotq.eat()