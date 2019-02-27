class Cat: #使用大驼峰
    '''定义了一个Cat类'''
    #属性

    #初始化对象
    def __init__(self,new_name,new_age):
        self.name = new_name
        self.age = new_age

    #方法
    def eat(self):   #函数定义在类里面就叫方法（）里面要有self,这里的self可以换成任何字母，但是通常写为self
        print("cat eat ...")
    def drink(self):
        print("cat drink kele ...")
    def introduce(self):
        print("%s的年龄是：%d" % (self.name, self.age))

    #创建对象
tom = Cat("汤姆",40)

#调用tom指向的对象中的 方法

tom.eat()   # d对象.方法
tom.drink()

#给tom指向的对象添加属性,实际上就是在申请的内存区域添加两个变量
#tom.name = "汤姆"
#tom.age = 40
#获取属性的第二种方法
tom.introduce()

lanmao = Cat("蓝猫",10)
#lanmao.name = "蓝猫"
#lanmao.age = 10
lanmao.introduce()


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

