lst = ["渣渣辉","古天绿","陈小春","彭佳慧","郑中基","胡辣汤"]
# lst.clear()
# print(lst)

# for el in lst: #for内部有一个变量来记录当前被循环的位置,索引
#     lst.remove(el)
# print(lst)

# ['古天绿', '彭佳慧', '胡辣汤']  之所以是这个结果是因为删除一个,另一个往前提变成0,正好错过了
# 直接删除是删不干净的,原因是每次删除都是涉及到元素的移动,索引在变


#正确删除方法
# 先把要删除的内容保存在一个新列表中,循环这个新列表,删除老列表

new_list = []
for el in lst:
    new_list.append(el)
for el in new_list:
    lst.remove(el)
print(lst)



lst = ["张无忌","张三丰","张翠山","张嘉译","刘嘉玲","刘能","刘老根"]

new_lst = []

for el in lst:
    if el.startswith("张")
        new_lst.append(el)

for el in new_lst:
    lst.remove(el)

print(lst)



dic = {"谢逊":"金毛狮王","韦一笑":"青翼蝠王","殷天正":"白毛鹰王","金花婆婆":"紫衫龙王"}

for k in dic:
    dic['谢逊'] = "张无忌他爹"

print(dic)

