#Author: kobe
names=["ZhangYang","Guyun","Xiangpeng","ChenRonghua","XuliangChen"]
print(names)
print(names[0],names[2])
print(names[1:3])

print(names[-1])
print(names[-3:-1])
print(names[-2:])

print(names[:3])

###############################################
names.append("LeiHaidong")
print(names)
names.insert(1,"ChenRonghua")
print(names)
names.insert(3,"Xinzhiyu")
print(names)
names[2] = "Xiedi"
print(names)
#names.remove("ChenRonghua")
#del names[1]
#names.pop(1)
print(names)
print(names.index("Xiedi"))
print(names[names.index("Xiedi")])
print(names.count("ChenRonghua"))

#names.clear()
print(names)
names.reverse()
print(names)
names.sort()
print(names)

names2 = [1,2,3,4]
names.extend(names2)
print(names,names2)