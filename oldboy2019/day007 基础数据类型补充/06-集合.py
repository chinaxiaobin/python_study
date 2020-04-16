
#set中元素是不重复的,无需的,里面的元素必须是可hash的(int str tuple bool)
#我们可以这样来记,set是dic类型的数据,但是不保存value, 只保存key,set也用{}表示

# 可变的是不可hash的  list set dic
# 不可变的是可hash的  tuple   str

#字典中的key是不重复的,可hash的
# dic = {"a":"娃哈哈","a":"爽歪歪"}
# print(dic) # key不会重复
#
# dic[[1,2,3]] = "娃哈哈"  #必须是可hash的
#
#
#
#
# 2.

# s = set()  #空集合
# s = {} #默认是字典
#
# s = {1,2,3,6,5,6,5,4}  #不重复  必须是可 hash的. 不能放列表, 可去重复
# print(s)
#
# #set其实就是不存value的字典,只存key
#
# #去重复
#
# lst = [1,2,3,4,4,5,5,5,5,6,7,7,7]
# s = set(lst)
# lst = lit(s)
# print(lst)



##增
#set集合是 无序的
s = {"赵本山","范围","小沈阳"}
s.add("宋清")
s.add("李小")
print(s)

s.update("汪峰")  #迭代更新 , 可以放元素 ("了六位","说是")
print(s)




# 删除
s = {'小沈阳', '峰', '宋清', '汪', '范围', '赵本山', '李小'}
item = s.pop() #随机删除一个
print(s)
print(item) #得到哪个被删除了

s.remove("小沈阳") #指定删除的元素
s.clear() #清空集合


#set集合没有索引,没办法定位一个元素去修改
#只能是s.remove()指定删除的元素然后s.add()指定去添加修改



#set是可迭代的 所以可以进行for循环
for el in  s:
    print(el)


#set集合本身是可以发生改变,不可hash的,但是我们 可以使用frozenset来保存数据
#frozenset是不可变得,也就是一个可hash的数据类型

s = frozenset(["赵本山","刘能"])
dic =  {s:'123'} #可以正常使用了
print(dic)

