class Cat():
    #属性


    #初始化对象
    def __init__(self,new_name,new_age):
        self.name = new_name
        self.age = new_age
    #描述信息

    def __str__(self):
        return "%s的年龄是：%d" %(self.name,self.age)
    #方法

    def eat(self):
        print("猫在吃...")
    def drink(self):
        print("猫在喝可乐...")

    def introduce(self):
        print("%s的年龄是：%d" %(self.name,self.age))

tom = Cat("汤姆",40)
tom.introduce()

lanmao = Cat("蓝猫",10)
lanmao.introduce()


print(tom)
print(lanmao)