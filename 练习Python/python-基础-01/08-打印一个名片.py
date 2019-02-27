# 先做啥再做啥，可以用注释搭框架
# 1.使用input获取必要信息
name = input("请输入你的名字:")
phone = input("请输入你的电话:")
wx = input("请输入你的微信:")
# 2.使用print来打印一个名片
print("=====================")
print("名字是:%s"%name)
print("电话是:%s"%phone)
print("微信好是:%s"%wx)
print("=====================")

"""
python2中input是将输入的内容当作代码了，而python3是把输入的内容当作一个字符串
name = input("请输入你的名字:")
如果输入1+4  然后打印name变量会得到结果5
如果输入laowang 会报错，这是因为
name = laowang   表示把laowang这个值赋给name，而laowang在内存中是没有的
Python2中使用 raw_input 才和python3中的input效果一样
"""