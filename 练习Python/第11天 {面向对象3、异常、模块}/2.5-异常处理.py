"""
异常：当python检测到一个错误时，解释器就无法执行了，反而出现了一些错误的提示，这就是异常

"""
try:
    open("xxxx.txt") #这个错误的名字是FileNotFoundError
    #print(num)
    print("-----1---------")
except NameError:  #except后面跟错误的名字，错误的名字首先不写try和except才能知道，如果定义了except不影响后面的2的执行
    #如果错误名字不一致那么后面的程序就无法执行
    print("如果程序出现异常正则处理")

print("--------2-------")