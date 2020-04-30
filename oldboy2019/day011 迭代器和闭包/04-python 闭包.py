def func():
    a = 10
    print(a)

func()
#print(a) #在外面是访问不到 局部变量的,局部变量是安全的


#全局变量可能会被修改  全局变量是 不安全的，看可能会被其他函数所更改
a = 10
def func():
    global a
    a = 20
    print(a)

func()
print(a)


#用闭包可以保护我们的变量

# 写法：在外层函数中声明一个变量 在内层函数使用或返回这个变量
#这个结构叫闭包
#1. 可以保护我的变量
#2. 可以让一个变量常驻内存

def outer():
    a = 10 # a是局部变量 会常驻内存
    def inner():
        print(a) #在内部是ii用的外面的变量
    return inner #返回乐内部函数

# ret收到的是innner的地址
ret = outer()
ret() #这里执行inner()
print("haha")
print("haha")
print("haha")
ret() #inner的执行时间是不确定的

print(ret.__closure__)  #有东西就是闭包，None就不是闭包

def haha():
    pass

print(haha.__closure__)


#闭包的应用： 保护变量  常驻内存



