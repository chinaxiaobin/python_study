#range()

for i in range(10): #范围是0-9, 帮我们生成数字
    print(i)

for i in range(3,8): #从3-8 没有8
    print(i)

for i in  range(5,10,2): #从5到10 ,步长是2
    print(i)

# range(边界) 从0到这个边界范围
# range(start,end) 从 start到end结束,不能到end
# range(start,end,stop) 从start到end结束,不能到end,步长是step

lst  = ["张无忌","张三丰","张翠山","张一山","张磊","张伟"]

# for el in lst:
#     print(el)  #这样循环,没有索引
#
# for i in range(6): #有索引了
#     print(lst[i])

for i in range(len(lst)):
    print(lst[i])


tu = ("首页","登录","注册","购物","退出")

for i in range(len(tu)):
    print(i,tu[i])

