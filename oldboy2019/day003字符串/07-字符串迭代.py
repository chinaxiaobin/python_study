s = "朱元璋朱棣朱允炆朱由校"
print(s[0]) #把s里的每个字符串显示一遍
print(s[1])

count = 0
# while count <=10: #随着字符串的变长,
# while count <= len(s) -1:
while count < len(s): #遍历字符串的第一种方法
    print(s[count])
    count = count+1

#
# 字符串是一类可迭代对象:可以一个一个往外取值的对象 就可以用for循环来遍历
# for 变量 in 可迭代对象:
# 把可迭代对象中的每一个对象,分别赋值给前面的变量,可以方便可迭代对象的遍历
for c in s:
    print(c)


# TypeError #这个报错, int object is not iterable
for i in 10:
    print(i)