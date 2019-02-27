class Dog(object):
    __instance = None
    def __new__(cls,name):  #这里的name只为了传递个参数，方便init方法调用，因为先调用new方法，不然无法执行
        if cls.__instance == None:
           cls.__instance = object.__new__(cls)
           return cls.__instance
        else:
            #return 返回上一次创建对象的引用
            return cls.__instance
    def __init__(self,name):
        self.name = name

dog1 = Dog("旺财")
print(id(dog1))
print(dog1.name)
dog2 = Dog("哮天犬")     #这样的话init执行了两次，需求是只执行一次
print(id(dog2))
print(dog2.name)