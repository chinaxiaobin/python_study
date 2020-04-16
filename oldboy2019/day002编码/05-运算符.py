"""
#1. 2**1 到 2**10 必须知道
#2.
!= 和 <> 都代表不等于
a = 10
b = 5
a += b  #实际上就是 a = a + b


# 3.
and 并且的意思,当左右两端同事为真,运算的结果才能是真
or 或者的意思,有一个为真,结果就是真
not 非真既假 非假既真

面试题:
运算顺序:
()  not  and or
"""
print(1 > 2 and 3 < 6 or 5 > 7 and 7 > 8 or 5 < 1 and 6 > 3)


# print(1 or 2 and 3)
# x or y ,如果x为0 ,则返回y,否则, 返回x,主要看第一个数字
# and 和 or相反
print(0 or 1) #1
print(0 or 2) #2
print(1 or 2) #1
print(1 or 0) #1

print(1 or 2 or 0 or 3 or 5)
print(0 or 0 or 5 or 3)
print(0 or 1 and 2) #先算and, 1 and 2,当成1 or 2 返回1 则and 返回2 , 0 or 2则返回2

# False:0  True: 1
print(1 > 2 and 3 or 5 and  4 > 6) # False
# 结果可能是数字 也可能是布尔值 True 或 False






