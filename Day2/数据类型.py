#Author: kobe

www.cnblogs.com/alex3714/articles/5465198.html

type(2**32)
#整型int

32位机器 -2**31--2**31-1
64位机器 -2**63--2**63-1

#浮点型
E表示10的幂，52.3E-4表示52.3*10**-4 科学计数法

#布尔值
真或假
1或0

>>> a=0
>>> if a :print("a")
...
>>> a=1
>>> if a:print("a")
...
a
>>>

##三元运算

>>> a,b,c = 1,3,5
>>> d = a if a>b else c
>>> d
5
>>>


#进制

二进制  八进制  十进制 十六进制

十六进制： 0 1 2 3 4 5 6  7  8 9 A B C D E F


字符串和二进制之间的转码

msg = "我爱北京天安门"
print(msg)  #打印变量的时候小括号内不能有引号
print(msg.encode(encoding="utf-8"))
print(msg.encode(encoding="utf-8").decode(encoding="utf-8"))

