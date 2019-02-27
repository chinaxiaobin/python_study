class Cat:
    def eat(self):
        print("eating...")
    def drink(self):
        print("drink....")
    def introduce(self):
        print("%s的年龄是：%d" %(self.name,self.age))

tom=Cat()
tom.eat()
tom.drink()

tom.name="汤姆"
tom.age=40

print("%s的年龄是：%d"  %(tom.name,tom.age))

tom.introduce()

lanmao = Cat()
lanmao.name = "蓝猫"
lanmao.age = 30
lanmao.introduce()