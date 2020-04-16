#Day3作业题

# 一.
name = "aleX leNb"
print(name.strip())
s1 = name.strip()       #1.去掉两边的空格
print(s1.lstrip("al"))  #2.去掉左边的al
print(s1.rstrip("Nb"))  #3.去掉右边的Nb


s2 = s1.lstrip("a")
s3 = s2.rstrip("b")
print(s3)               #4.去掉变量开头的a和最后的b 并输出处理结果

print(name.startswith("al"))  #5.判断是否以al开头
print(name.endswith("Nb"))  #6.判断是否以Nb开头


print(name.replace("l","p"))  #7.将所有的l替换为p
print(name.replace("l","p",1)) #8.只讲第一个l替换为p

print(name.split("l")) #9.将所有l分割
print(name.split("l",1)) #10. 根据第一个l分割

print(name.upper()) #11.变大写
print(name.lower()) #12.变小写

print(name.capitalize()) #13.将首字母大写

print(name.count("l")) #14.计算l出现几次

print(name.count("l",1,4)) #15. 前4位l出现几次
print(name.index("N")) #16. 找到N的索引,找不到则报错
print(name.find(""))  # 17. 找到N的索引,找不到则报-1

print(name.find("X le"))  #18. 找到X le的位置

print(name[2]) #19.请输出 name 变量量对应的值的第 2 个字符
print(name[:3]) #20.请输出 name 变量量对应的值的前 3 个字符

print(name[-3:-1])#21.请输出 name 变量量对应的值的后 2 个字符?

print(name.find("e"))#22. 请输出 name 变量量对应的值中 "e" 所在索引位置?

# 二.

s = "123a4b5c"

s1 = s[0:3]
print(s1)
s2 = s[3:6]
print(s2)
s3 = s[::2]
print(s3)
s4 = s[1:6:2]
print(s4)

s5 = s[-1]
print(s5)

s6 = s[-3::-2]
print(s6)


# 三.

# 使⽤用while和for循环分别打印字符串串s="asdfer"中每个元素

# s="asdfer"
# count = 0
# while 1:
#     print(s[count])
#     count = count+1

s="asdfer"

for i in s:
    print(i)



#四. 使⽤用for循环对s="asdfer"进⾏循环，但是每次打印的内容都是"asdfer"

s = "asdfer"
for i in s:
    print(s)

#五. 使⽤用for循环对s="abcdefg"进⾏行行循环，每次打印的内容是每个字符加上sb 例例如:asb, bsb，csb,...gsb。

s="abcdefg"
for i in s:
    print(i+"sb")

#6. 使⽤用for循环对s="321"进⾏行行循环，打印的内容依次是:"倒计时3秒"，"倒计时 2秒"，"倒计时1秒"，"出发!"。


s = "321"
for i in s:
    print("倒计时"+i+"秒")
print("出发")

# 7.
content = input("请输入内容计算两个数相加")
cont = content.split("+")
a = int(cont[0].strip())
b = int(cont[1].strip())
print(a+b)

# 8.

