#实参的分类：
# 1.位置参. 按照位置，给形参赋值
# 2.关键字参数.按照形参的名字给参数赋值
# 3.混合参数,位置参数必须放在前面，关键字参数必须放在后面

def chifan(good_food,no_good_food,drink):
    print("我要吃",good_food,no_good_food,drink)

chifan("米饭","炸鸡","冰峰")
chifan(drink="哇哈哈",no_good_food="薯条",good_food="盖浇饭")
chifan(drink="可乐","小蜜蜂","辣条")

#形参的分类(3大类)：
#1.位置参数 按照位置来声明形参
#2. 默认值参数 当给参数传递值的时候  默认值不起作用 不给值，默认值起作用 保证有个值至少能用
# 顺序：位置参数必须放在前面 默认值参数放在后面
def regist(name,age,sex):  #比如本班男生特别多，则默认是男
    print(name,age,sex)

regist("刘伟", 22, "男")
regist("李铁帅", 27, "男")
regist("高晓燕", 18, "女")

# 函数：对功能或者动作的封装

#登录认证

def login(username,password):
    if username == 'alex' and password == '123'
        return True
    else:
        return False


#使用场景
name = input("请输入你的账号")
pws = input("请输入那你的密码")
if login(name,pws):
    print("进入主页")
else：
    print("用户名或密码错误，请重新登录")



# f(x) = x + 1
# f(2) = 2 + 1

def f(x):
    return x + 1

ret = f(2)
print(ret)
#或直接使用 print(f(2))


s = "你好啊我叫赛丽亚"
print(len(s))

def my_len(s):
    count = 0
    for e in s:
        count += 1
    return count
print(my_len(s))


