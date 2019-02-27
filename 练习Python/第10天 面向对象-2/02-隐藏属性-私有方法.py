class Dog():
    #私有方法
    def __send_msg(self):
        print("_______正在发送短信_______")
    #公有方法
    def send_msg(self,new_money):
        if new_money > 1000:
            dog.__send_msg()
        else:
            print("余额不足，请充值")
dog = Dog()
dog.send_msg(1001)


#<==== 定义一个带__双下划线的私有方法，里面由我们的信息，然后定义一个公有方法给上条件
#是否满足来发送我们的私有方法信息，一般这是编程的思想