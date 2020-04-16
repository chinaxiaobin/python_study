f = open("/data/test.123", mode="r", encoding="utf-8") #如果不写utf-8 默认字符跟着操作系统走,中文系统是GBK, GBK不能直接转utf-8
# content = f.read()  #一次读取所有内容 缺点: 1.读取大的文件的时候,内存容易溢出 2.操作比较麻烦
# content = f.read(3) #读取3个字符
# line1 = f.readline()
# line2 = f.readline()
# print(line1)  # 默认readline()函数读取的一行内容有换行符\n
# print(line2)
#
# print(line1, end=" ") #把最后打印的换行符换成空格 默认后面的符号会在第二行
# print(line2, end=" ")


# line1 = f.readline().strip()  #去掉空白: 包括空格, \t, \n
# line2 = f.readline().strip()
# print(line1)
# print(line2)

# content = f.readlines() #也是全部加载进来了,得到的是列表
# print(content)

# f 需要是一个可迭代对象

for line in f: #内部调用的其实就是readline()
    print(line)

f.close() # 关闭