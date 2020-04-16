s = "太白金星"
print(s[::-1])
print(s)

s = "alex is not a good man Tory is good man"
s1 = s.capitalize()  #首字母大写
print(s)  #字符串s是不改变的
print(s1)

s1 = s.upper()  #全部大写  使用场景忽略大小写
print(s1)

s1 = s.lower() #小写字母
print(s1)
#
# while True:
#     content = input("请输入你要喷的内容(输入Q退出):")
#     #if content == 'Q' or content == 'q':
#     if content.upper() == 'Q':  #当用户输入q或Q的时候退出,这里忽略大小写
#         break
#     print(content)


# s = "alex is not a good man Tory is good man"
# s1 = s.swapcase() #大小写互换
# print(s1)
#
#
# s.lower()
# s.casefold()  # 也是转换成小写,支持的文字比较多
# s.title() #每个单词的首字母边大写
#
# s = "class apple banana oranger pear alex wusir"
# s1 = s.title()
# print(s1)


s = "刘伟"
# center(self, width, fillchar) 使用方法 self是自己,width宽度 fillchar填充的字符
s1 = s.center(20)
print(s1)
s1 = s.center(20,"*")
print(s1)
s1 = s.center(3,"*") #把字符串拉长成3个单位 用*填充
print(s1)

#去空格 只会去掉左边和右边的空白(空格或\t),不会去掉中间的
s7 = "   你好啊,  我叫赛利亚   "
s = s7.strip()
print(s)

s7 = "\t你好啊,  我叫赛利亚   "
print(s7)
s = s7.strip()
print(s)

# s = s7.lstrip()  去掉左边空格
# s = s7.rstrip()  去掉右边空格

#模拟登陆
#用户输入的内容是无法保证合法的,需要进行处理和判断
# username = input("请输入你的用户名:").strip()
# password = input("请输入你的密码:").strip()
# # if username == "alex" and password == "123":
# if username == "alex" and password == "123":
#     print("成功")
# else:
#     print("失败")



# s = "刘伟很帅刘伟"
# s1 = s.strip("刘") #去掉指定的字符串
# print(s1)


#字符串替换
# s = "alex_wuusir_ritian_taibai_evaj_eggon"
# s1 = s.replace("taibai","taihei")
# print(s1)
# s1 = s.replace("i","SB",2) #2表示换几次
# print(s1)

#字符串切割

s = "alex_wuusir_ritian_taibai_evaj_eggon"
lst = s.split("ritian")  #切割后的字符串会装在列表中
print(lst)  #刀有多宽,就要损失掉多少,上面损失的是ritian

lst = s.split("_")
print(lst)
print(lst[0])

print("周润发\n周星驰周笔畅周杰伦") # \n是换行

s = "周润发周星驰周笔畅周杰伦"
s1 = s.split("周杰伦")
print(s1)


#格式化输入
print("我叫%s,我今年%d岁了,我喜欢干%s" % ("alex",18,"python")) #之前的写法 数据和格式分离了

print("我叫{},我今年{}岁了,我喜欢干{}".format("alex",18,"python"))

print("我叫{1},我今年{0}岁了,我喜欢干{2}".format("alex",18,"python"))


print("我叫{name},我今年{age}岁了,我喜欢干{hobby}".format(name="alex",age=18,hobby="python"))


#字符串查找

s = "今天的内容非常简单,你们信吗? 作业也很容易,就是整理不太好"
print(s.startswith("今天")) #以什么开头
print(s.endswith("太好了"))  #以什么结尾

s = "胡辣汤 炸鸡 啤酒 烤鸭 炸鸡 锅包肉"
print(s.count("炸鸡"))  #计数


print(s.find("胡辣汤")) #出现的位置  #如果找不到返回-1
print(s.index("胡辣汤")) #出现的位置  #如果找不到返回报错

#条件判断


s = "abcdefg"
print(s.isalpha())
print(s.isdigit()) #是否数字 不识别 一 二
print(s.isnumeric()) #是否数字 可以识别中文 一 二  壹 贰, 不过两字不认识


#计算字符串的长度


s = "我是上帝, 你也是上帝"
print(len(s)) #内置函数len(字符串),返回给你字符串的长度



#迭代















