#元组就是不可改变的列表 元组使用()表示,元素和元素之间使用逗号隔开,数据类型没有限制,可以叫只读列表

#清朝的皇帝(努尔哈赤 皇太极 顺治 康熙 雍正 乾隆)

huang = ("努尔哈赤", "皇太极", "顺治", "康熙", "雍正", "乾隆","嘉庆","道光","光绪","咸丰")
# huang[1] = "朱元璋" #报错 tuple不支持元组的修改
print(huang)

#print((8+3)*7)  #小括号不仅表示元组还可以表示优先级

tu = (1)
print(type(tu))  #只有1个元素会先表示优先级表示整型,所以加逗号

tu = (1,)
print(type(tu))

tu = tuple()  #空元组表示   列表可以直接使用[]表示


# 元组也有索引和切片 和列表一样和字符串一样

tu = ("iphone","nokia","砸核桃","Lenovo","HTC","Honor")

print(tu[2])
print(tu[1:3])

print(tu[1:5:2])


# 元组不可变指的是第一层元素不可变
tu = (1,2,5,["胡辣汤","猪蹄子","酱猪肘","米饭","炸鸡"])

# tu[3] = "娃哈哈"  #报错,第一层没法改变 第二层能否改变取决于数据类型
# print(tu)

tu[3][0] = "科比"
print(tu)
tu[3].append("锅包肉")
print(tu)

#元组只能 count()  index()  不能sort

#count计算某个元素出现多少次
print(tu.count(1)) #查看1元素共有几个
print(tu.index(2)) #查看2这个元素在索引哪个位置

# sort使用  默认元组不能sort
# tu.sort()
# print(tu)

tu = ("孙悟空","白骨精","哪吒","二师兄")
for el in tu: # element元素
    print(el)

