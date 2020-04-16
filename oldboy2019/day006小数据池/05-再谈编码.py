# 1. ASCII: 8bit 1byte 英文字母 数字 特殊字符  存不了中文,存中文的是GBK
# 2. GBK: 16bit 2byte 主要是存中午,日文 韩文,繁体字, 中文的特殊字符
# 3. UNICODE: 32bit 4byte 万国码
# 4. UTF-8 可变长度的UNICODE
#         英文: 8bit 1byte
#         欧洲文字: 16bit 2byte
#         中文: 24bit, 3byte
#
# GBK和UTF-8不能直接互换


#在python2里,默认编码是ASCII
#默认unicode 32bit, 比较浪费, 在python3中unicode是可以使用的,默认用的是Unicode,我们文件的代码要用utf-8
#在内存跑起来是unicode跑的,主要是定长


# 1. 为什么要编码 把unicode转换成utf-8

# s = "刘海很皮"  # 4*3=12字节
# abc = s.encode("UTF-8") #encode之后的结果是bytes类型 依然是原来的字符串
#
# print(abc)

# 解码
abc = b'\xe5\x88\x98\xe6\xb5\xb7\xe5\xbe\x88\xe7\x9a\xae'
s = abc.decode("UTF-8") #解码 用什么编码就用什么解码
print(s)


s = "赵瑞鑫"
print(s.encode("GBK")) # b'\xd5\xd4\xc8\xf0\xf6\xce'
# GBK的编码不能用UTF-8去解码


# GBK的编码 把这句话变成UTF-8
bs = b'\xd5\xd4\xc8\xf0\xf6\xce'

#先解码
s = bs.decode("GBK")
bs2 = s.encode("UTF-8")
print(bs2)