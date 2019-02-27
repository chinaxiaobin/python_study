class Car_store(object):
    def order(self,car_type):
        if car_type == "索纳塔":
            return Suonata()
        elif  car_type == "名图":
            return Mingtu()
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

car_store = Car_store()
car = Car_store.order("索纳塔")
car.move()
car.music()
car.stop()


