"""
需要，如果再加一辆IX35呢， 需要修改商店类和添加下面的品牌类，
这样两个类的耦合性比较高，修改一个必须修改另一段代码
"""
"""
利用函数解耦
"""
class Car_store(object):
    def order(self,car_type):
        return select_car_by_type(car_type)
def select_car_by_type(car_type):
        if car_type == "索纳塔":
            return Suonata()
        elif  car_type == "名图":
            return Mingtu()
        elif  car_type = "IX35":
            return IX35()
class Car()
    def move(self):
        print("车在移动")
    def music(self):
        print("正在听音乐")
    def stop(self):
        print("车在停止")

class Suanata(Car):
    pass
class Mingtu(Car):
    pass
class IX35(Car):
    pass

car_store = Car_store()
car = Car_store.order("索纳塔")
car.move()
car.music()
car.stop()


