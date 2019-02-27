class Cat: #使用大驼峰
    '''定义了一个Cat类'''
    #属性

    #初始化对象
    def __init__(self,new_name,new_age):
        self.name = new_name
        self.age = new_age


    def __str__(self):
        return("%s的年龄是：%d"%(self.name,self.age))
    #方法
    def eat(self):   #函数定义在类里面就叫方法（）里面要有self,这里的self可以换成任何字母，但是通常写为self
        print("cat eat ...")
    def drink(self):
        print("cat drink kele ...")
    def introduce(self):
        print("%s的年龄是：%d" % (self.name, self.age))

    #创建对象
tom = Cat("汤姆",40)


lanmao = Cat("蓝猫",10)

print(tom)   #打印的是str的return语句

 #当我们print打印一个对象的时候，会打印这个对象的描述信息，就是__str__定义的描述信息
print(lanmao )
'''
创建对象的过程：
 
首先定义一个类Cat,只是定义，但是不执行---->直接到tom = Cat(),先执行等号右边
---》向操作系统申请一块内存创建对象====》返回对象的引用-----》tom = 创建出的对象
的引用

后面是对象.方法（就是我们类里面创建的方法）



1. 创建一个对象
2. python会自动调用__init__方法 或叫魔法方法
3. 返回创建的对象的引用给tom 或蓝猫

'''

