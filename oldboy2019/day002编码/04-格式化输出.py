"""
name = "alex"
xingrong = "愚蠢"
s = "%s是一个很%s的人" % (name, xingrong)
# %s表示是一个占位,我一会用一个字符串填充进去
# 空格 % 空格(name, xingrong)
print(s)
"""

# #示例1:
# #让用户输入 名字,年龄,爱好, 格式化输出成 我叫xxx, 我喜欢xxx, 我今年xxx岁了
#
# name = input("请输入你的名字:")
# age = int(input("请输入你的年龄:"))
# love = input("请输入你的爱好:")
#
# people = "我叫%s, 我喜欢%s,我今年%d岁了" % (name, love, age)
# print(people)
#
# # s%可以接收任何类型  所以上面可以都用%s
# # %d必须是数字

# print("大家好,我叫%s, 我已经学习python 15%%了" %("李彬")) #当语句中出现占位符的时候,要想使用%的原始意义需要写两个%%
# print("大家好,我已经学习python 15%了") #没有占位符,则打出原始意思
# print("我叫%s,今年%d了" %("李彬", 19))


