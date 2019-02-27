'''
class 类名：
    #属性
    #方法

'''

class Cat: #使用大驼峰
    #属性
    #方法
    def eat(self):   #函数定义在类里面就叫方法（）里面要有self
        print("cat eat ...")
    def drink(self):
        print("cat drink kele ...")

#创建对象
tom = Cat()

#调用tom指向的对象中的 方法

tom.eat()   # d对象.方法
tom.drink()




'''
创建对象的过程：
 
首先定义一个类Cat,只是定义，但是不执行---->直接到tom = Cat(),先执行等号右边
---》向操作系统申请一块内存创建对象====》返回对象的引用-----》tom = 创建出的对象
的引用

后面是对象.方法（就是我们类里面创建的方法）

'''
