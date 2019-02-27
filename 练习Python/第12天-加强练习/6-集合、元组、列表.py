"""
列表：list, 有增删改查  []
元组：tuple  不能修改  ()
集合：set   不能重复，支持增删改查 ｛｝
字典：dict  键值对　{"a":1,"b":2}

"""

#列表去重
a = [11,22,33,44,11,22,33]
b =  []
for i in a:
    if i not in a:
        b.append(i)
print(b)

#集合去重
c = set(a)
print(a)

list(set(a))  #无序的