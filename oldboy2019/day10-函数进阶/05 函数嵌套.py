#def func1():
#     print("我是func1")
#
# def func2():
#     print("我是func2")
#     func1()
#
# def func3():
#     func2()
#     print("我是func3")
#
# func3()

# 这样的代码不是嵌套，这是互相调用

#函数可以互相嵌套
#
# def outer():
#     def inner():
#         print("我是内部")
#     print("我是外部")
#     inner()
# outer()


# def outer():
#     print("我是外面的")
#     def inner_1():
#         print("我是里面的1")
#         def inner_2():
#             print("我是里面得到2")
#         inner_2()
#     inner_1()
#     print("我是外面的收尾")
#
# outer()


# a = 10
# def func()
#     a = 20
#     print(a)
# print(a)
# func()
# print(a)



# a = 10
# def func():
#     global a #表示再当前作用域中的使用的a是全局中的变量
#     a = 20  #现在这个a是全局的
#     print(a)
#
# print(a)
# func()
# print(a)


def outer():
    a = 10
    def inner():
        a = 20
        print(a)
    print(a)
    inner()
    print(a)
outer()


