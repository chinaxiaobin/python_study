#coding=utf-8

#try是可以嵌套的

try: #必须try里的代码出现异常才会匹配下面的错误
    11/0
    open("xxx.txt")
    #print(num)
    print("----1----")

except (NameError,FileNotFoundError): #如果匹配多个错误，利用小括号元组放在一起
    print("如果捕获到异常后做的处理....")
#except Exception:
except Exception as ret:  # as后面的变量名字随便其，为了输出错误的名字
    print("如果用了Exception,那么意味着只要上面的except没有捕获到异常，这个except一定会捕获到")
    printe(ret)
else: #else这句可以不写
    print("没有异常才会执行的功能")

finally: #不过try里面的语句有没有异常都会执行，使用场景：
    #比如读取文件 读取中出现异常最终需要关闭文件，读取完成最终也需要关闭文件
    print("----finally---")


# 假如有3个函数，函数之间1-2-3调用，会传递到调用方的异常 1有异常可以传递到3，3没有
# 异常处理，会传递给python默认的系统异常
