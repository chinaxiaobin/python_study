lst = [ "情深深雨蒙蒙", "还珠格格", "夏雨荷", False, True, 50000000, 12.56, [ "国际章", "迪丽热巴", "古力娜扎" ] ]

print(lst)

#列表也有索引

lst = [ "上海滩", "西游记", "家有儿女", "奥特曼", "包青天", "少年包青天" ]
print(lst[3])
print(lst[-4])
#print(lst[8])  #报错 list index out of range
print(lst[-1][1:3])  #显示年包两个字


#切片
print(lst[1:3])  #切片出来的是列表 字符串切出来的是字符串 元组切出来的是元组
print(lst[1:5:2])
print(lst[-1:-4:-2])

#索引和切片 参照字符串


