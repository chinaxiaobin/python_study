# def chi(good_food, no_good_food, zero_food, drink):
#     print("我要吃", good_food, no_good_food, zero_food, drink)
#
# chi("大米饭", "辣条", "方便面", "可乐")


def chi(*food):  #表示的是不定参数,可以传递任意个信息,接收到的是元组
    print("我要吃", food)

chi("一大锅米饭", "一小锅米饭", "一箱辣条")


# * 表示接收位置参数的动态传参


# 位置, *args  默认值   #顺序
# 如果默认值参数在*args前面,如果想让默认值生效 *args将永远接不到值

def func(a, b, c = 5, *args):
    print(a, b, c, args)

func(1, 2, 3, 4, 5)

def func(a, b,  *args, c = 5):
    print(a, b, c, args)

func(1, 2, 3, 4, 5, c = 10)



def func(*args, a, b):
    print(args, a, b)

func(1, 2, 3, 4, 5, a=6, b=7)   #位置参数必须放在前面


# 实参: 1,位置 2, 关键字 3,混合

# 传参的顺序很重要
# 关键字的动态传参
# *args 位置参数的动态传参  接收到的是元组
  ### 位置, *args  默认值   #顺序
# **kwargs 关键字的动态传参  接收到的是字典
  ### 位置参数 *args   默认值  **kwargs


def func(**kwargs):
    print(kwargs)

func(a=10, b=20, jay="周杰伦", jj="林俊杰")


#无敌模式,所有的参数都能接收
def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, 5, jj="陶喆", jay="zhoujielun", soup="hulatang")



#扩展

def func(*args):  #在这里其实相当于把传来的参数做了一次聚合,聚合成一个元组
    print(args)

lst = ["大白菜", "小白菜", "娃娃菜", "大头菜"]

func(lst[0], lst[1], lst[2], lst[3])

func(*lst) #在实参位置 *表示打散 , 列表和元组都可以打散,打散的是可迭代对象


def func(**kwargs): #**把接收到的关键字参数打包(聚合)成字典
    print(kwargs) #一定是字典

dic = {"张无忌": "明教教主",  "谢逊": "金毛狮王", "范瑶": "光明右使"} #key不可以是纯数字, 数字不能作为变量

func(张无忌=dic['张无忌'], 谢逊=dic['谢逊'], 范瑶=dic['范瑶'])
func(**dic)  # 这里的**是把字典打散,字典的kkey作为参数的名字,字典的值作为参数的值传递给形参

'''
#总结
#在形参上
# 1.位置参数
# 2.默认值参数
# 3.动态参数
      1. *args  位置参数的动态传参,系统会自动的把所有的位置参数聚合成元组
      2. **kwargs 关键字的动态传参,系统会自动把所有的关键字参数聚合成字典
      3. def fun(*args, **kwargs):  无敌传参
      4. 顺序: 位置参数 *args 默认值 **kwargs
      5. 在使用的时候,可以任意的进行搭配

  4. 在实参上, *, ** 表示打散, 在形参, * ,**表示聚合
'''

