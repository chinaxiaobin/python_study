"""
单例对象：不管怎么创建都指向同一个对象
"""
class Dog(object):
    __instance = None
    def __new__(cls):
        if cls.__instance == None:
           cls.__instance = object.__new__(cls)
           return cls.__instance
        else:
            #return 返回上一次创建对象的引用
            return cls.__instance

dog1 = Dog()
print(id(dog1))
dog2 = Dog()
print(id(dog2))