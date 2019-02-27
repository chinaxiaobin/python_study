class Dog():
    def set_age(self,new_age):
        if new_age >= 0 and new_age <= 100:
            self.age = new_age
        else:
            self.age = 0
    def get_age(self):
        return self.age

#<======= 隐藏属性，先定义一个属性，其中里面含有条件判断，然后定义第二个方法 return其 值
#<======= 传递值给第一个方法，利用变量获取第二个方法，打印变量的值
dog = Dog()

dog.set_age(10)
age = dog.get_age()
print(age)

dog.set_age(-10)
age = dog.get_age()
print(age)