#while循环生成列表
a = []
i = 10
while i<18:
    a.append(i)
    i+=1
print(a)

#for循环生成列表
b = []
for i in range(10,18):
    b.append(i)
print(b)

# 列表生成式
c = [i for i in range(10,18)]  # 第一个i就是决定往列表插入的元素
print(c)

#结果：
#[10, 11, 12, 13, 14, 15, 16, 17]

"""
注意点：
range风险：
这个问题只在python2中存在，假如取非常大的数值，python2会申请很大的一块内存空间占用，python3默认不会
去直接生成，而是等你需要的时候，并且把你指定的需要的值生成出来，这样占用的空间就非常小

上面的while循环和for循环都是申请一块内存空间占用，列表生成式是当你需要的时候才会去申请
"""
d = [i for i in range(10) if i%2==0]
print(d)

e = [i for i in range(3) for j in range(2)]
print(e)


"""
# 上面的列表生成式就相当于下面的循环
e = []
for i in range(3):
    for j in range(2):
        e.append((i,j))
"""


f = [(i,j) for i in range(3) for j in range(2)]
print(f)
# [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
# 说明 i没执行一次，后面的的j都执行完，也就是2次
