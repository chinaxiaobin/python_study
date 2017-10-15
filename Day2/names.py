#列表
names = ["ZhangYang", "Guyun", "Xiangpeng", "ChenRonghua","Xuliangchen"]
#取ZhangYang,Xiangpeng
print(names[0],names[2])
#取ZhangYang,Xiangpeng一块取出来
print（names[1:3]） #顾头不顾尾，切片


'''
print(names[-1]) #取最后一个值
print(names[-3:-1]) #因为顾头不顾尾所有取不出Xuliangchen,我现在想把最后两个取出来
print(names[-2:])

print(names[0:3])
print(names[:3])
'''


#增删改查
print("-----",names)
names.append("LeiHaidong") #插在列表后面
names.insert(1,"ChenRonghua") #插在特定位置，根据序号插入即可,不能批量插入
names.insert(3,"Xinzhiyu")
#改
names[2] = "XieDi"
#切片
print(names)
#删除-1种
#names.remove("ChenRonghua")
#删除-2
#del names[1]
#删除-3种
#names.pop(1) #和del names[1]差不多，默认删除最后一个
print(names)

#查找
print(names.index("XieDi"))
print( names[names.index("XieDi")] )
#统计
print(names.count("ChenRonghua"))
#清空
names.clear()
print(names)
#反转
names.reverse()
print(names)
#按字母顺序排序     特殊符号>数字>大写>小写
names.sort()
print(names)

#列表合并
names2 = [1,2,3,4]
names.extend(names2)
print(names,names2)

#删除变量
del names2