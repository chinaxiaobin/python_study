class Animal(object):
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def sleep(self):
        print("睡")
    def run(self):
        print("跑")
class Dog(Animal):
    def bark(self):
        print("汪汪叫")
class Xiaotq(Dog):
    def fly(self):
        print("飞")
xiaotq = Xiaotq()
xiaotq.eat()
xiaotq.bark()
xiaotq.fly()