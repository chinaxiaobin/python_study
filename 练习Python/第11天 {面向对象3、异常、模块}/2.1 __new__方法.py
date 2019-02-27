class Dog(object):
    def __init__(self):
        print("---init--方法")
    def __del__(self):
        print("---del--方法")
    def __str__(self):
        print("---str--方法")
        return "对象的描述信息"
    def __new__(cls):  #cls此时是Dog指向的哪个类对象
        #print(id(cls))
        print("---new--方法")
        return object.__new__(cls)
#print(id(Dog))
xtq =Dog()
"""
Dog（）相当于要做3件事情：
1. 调用__new__方法来创建对象，然后找了一个变量来接收__new__的返回值，
   这个返回值表示创建出来的对象的引用
    
2. __init__（刚刚创建出来的对象的引用）

3. 返回对象的引用给 xtq这个变量
"""

"""
总结：
__new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供

__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，或者直接是object的__new__出来的实例

__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值

我们可以将类比作制造商，__new__方法就是前期的原材料购买环节，__init__方法就是在有原材料的基础上，加工，初始化商品环节
"""