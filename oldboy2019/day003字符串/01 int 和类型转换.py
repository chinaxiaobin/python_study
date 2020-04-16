# # bit_length() 二进制的长度
#
# a = 4 # 10进制2  2进制 100
# print(a.bit_length())

# 把字符串转出成int
# a = "10"
# print(type(int(a)))

# # 把int 转换成字符串
#
# a = 10
# print(type(a))
# print(type(str(a)))
#
#
# #结论:想转化成xxx数据类型  xxx(目标)
#
# a = 10
# b = bool(a)
# print(b)
#
# a = True
# print(int(a))


# 结论 True 是1  False是 0
# 数字只有0 是False  其他都是 True 无论正整数还是负整数还是空格还是任何字符都是True
# 可以当做False来用的数据: 0  ""
# 所有的空的东西都是False   0  ""  []  ()   {}  None
# print(bool(0))
# print(bool(""))
# print(bool([]))  #空列表
# print(bool(()))  #空元祖
# print(bool(None))


#
# while 1:  # 1 和 True的效率  1的效率比True高一点   因为True多了个转换 1 的过程
#     print("还我钱")

