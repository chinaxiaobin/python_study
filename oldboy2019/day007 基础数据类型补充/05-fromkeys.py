#
# d = {}
#
#
# # fromkeys正常来说应该是类名来访问的
#
# #dd = d.fromkeys("马化腾","周芷诺") # fromkeys是一个类方法,作用是创建新字典
# dd = d.fromkeys(["马化腾","are you ok"],"周芷诺")
# print(d) #原字典没有改变
# print(dd) #新的字典是通过第一个参数的迭代,和第二个参数组合成key:value创建新字典
#
#
# dd = d.fromkeys(["马化腾","are you ok"],"周芷诺")


d = dict.fromkeys(["娃哈哈","爽歪歪"],[]) #所有的key用的都是同一个列表,改变其中一个,另一个也跟着改变
d["娃哈哈"].append("张无忌")
print(d)

print(id(d['娃哈哈']),id(d['爽歪歪']))