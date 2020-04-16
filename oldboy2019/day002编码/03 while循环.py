#
# print("你是不是傻")
# print("下路支援,你不来?")
# print("xsdfesf3a!@$@")

"""
while循环

while 条件:
    代码块
流程: 判断条件是否为真,如果真,执行代码块,然后再次判断条件是否为真,如果真继续执行代码
     直到条件变成了假,循环退出

#死循环
while True:
    print("!#@#$@!")
"""
# Count = 0
# while Count <= 100:
#     print("!#@#$@!1")
#     Count += 1




#count的作用: 计数 控制循环范围

#从1-100
# count = 1
# while count <= 100:
#     print(count)
#     count = count + 1

# 求1+2+3+4+....100 = ?

# count = 1
# sum = 0
# while count <= 100:
#     sum = sum + count #累加运算的思想
#     count = count + 1
# print(sum)


# 让用户喷的内容,不停的喷
#
# while True:
#     content = input("请输入你要跟对方说的话(输入Q退出): ")
#     if content == "Q":
#         #exit(0)  #退出程序
#         #break    #退出本层循环,不会对外层循环产生影响, 毁灭性的
#         continue  #停止当前本次循环,继续执行下次循环, 暂时性的
#     print(content)
# print("我去吃饭了") #输入Q是直接全部退出,这句是不执行的
#                   #换成break退出循环,然后打印print

content = input("请输入你的评论信息:")
if "金三胖" in content:
    print("对不起,你的评论包含敏感词汇")
else:
    print(content)