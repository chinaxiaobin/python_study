dic = {"jj":"林俊杰","jay":"周杰伦","tz":"陶喆",1:"哈哈"}

#[]:"胡辣汤" 这样是不行的,列表是可变的,unhash type, 必须是可hash的不可改变的

# 字典的新增


dic = {}
dic['徐峥'] = "人在囧途"  #直接用key往里面存数据即可
print(dic)
dic['黄渤'] = "疯狂的石头"
print(dic)
dic["王宝强"] = "天下无贼"
dic["王宝强"] = "士兵突击"  #如果key已经存在,那么会替换掉原来的value

dic.setdefault("黄秋生","头文字D")
dic.setdefault("黄秋生","无间道") #如果key已经存在,不会替换掉原来的value
print(dic)


