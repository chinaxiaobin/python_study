def chi():
    print("吃月饼")

print(chi)  #得到一个内存地址 ，发现这个是一个函数，就会去执行

fn = chi  #函数名可以进行赋值

a = 10
b = a #和这个套路很像
chi()
fn()


# 函数名可以像变量名一样进行使用


def func1():
    print("我是一个单纯的函数")

def func2(abc):
    print("我是func2", abc)

a = "苹果"
func2(a)
func2("苹果")
func2(func1)  #func1是函数的内存地址，则abc接收的是一个函数的内存地址
func2(func1())  #

# 函数名可以像变量一样进行参数的传递

def outer():
    def inner():
        print("我是里面")
    return inner  #这里inner是内存地址

ret = outer() #outer得到的结果是inner
ret()  #执行的是inner()函数

#或者
outer()()  #小括号表示的是执行

#
# a = "周润发"
# b = "蓝洁瑛"
# c = "春三十娘"
# d = "简直了"
#
# lst = [a, b, c, d]
# for el in lst:
#     print(el)

def chi():
    print("吃饭")

def he():
    print("喝饮料")

def du():
    print("赌是不好的")

def chou():
    print("少抽点烟")

lst = [chi, he, du, chou]
for el in lst:
    el()
print(lst)


def panpan():
    print("我是盼盼")
def xiaoping():
    print("我是小平")
def daguanren():
    print("我是大官人")

def wangpo(nv,nan):
    nv()
    nan()

wangpo(xiaoping, daguanren)



a = chi
haha = a
hehe = haha
bilibili = hehe

bilibili()
print(bilibili.__name__)  # __name__ 函数名


def play(wanjv1,wanjv2):
    '''  #注释相关的，会提前给一些预内容
     这是关于玩的函数
    :param wanjv1:  玩具1
    :param wanjv2:  玩具2
    :return:  开心
    '''

    print("我要玩荡秋千")
    return "开心"

#play("独木桥","独轮车")
print(play.__doc__) #打印文档
print(str.join.__doc__) #打印官方文档

#注释很重要