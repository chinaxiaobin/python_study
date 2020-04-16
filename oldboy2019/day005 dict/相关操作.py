dic = {"汪峰":"大陆音乐半壁江山","周杰伦":"亚洲音乐天王","罗志祥":"亚洲舞王"}
print(dic.keys()) # dict_keys(['汪峰', '周杰伦', '罗志祥'])  像列表但不是列表

# 对字典的遍历

for key in  dic.keys():
    print(key)   #拿到key
    print(dic[key])  #拿到value



print(dic.values())

for value in dic.values():
    print(value)


print(dic.items())

for item in dic.items():   # 拿到的是key和value
    print(item)  #得到的是元组
    print(item[0],item[1])


# a = 10
# b = 20

a, b = 10, 20
print(a)
print(b)

a, b = (10, 20)  # 解构,解包  换成列表也支持   a,b = [10, 20]

# 前面的变量的个数和后面解包的个数要一致
print(a)
print(b)

for item in dic.items():
    print(item)
    k,v = item
    print(k)
    print(v   #这样利用解包可以拿到key 和value


for k,v in dic.items():   #当需要遍历字典 或在操作中涉及到key和value的时候
    print(k)
    print(v)


# 字典本身是一个可迭代对象

for el in dic:
    print(el)   #直接循环字典,默认拿到是key
    print(dic[el])