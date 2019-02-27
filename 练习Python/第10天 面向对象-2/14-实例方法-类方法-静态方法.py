class Game(object):
    #类属性
    num = 0
    #实例方法
    def __init__(self):
        #实例属性
        self.name = "laowang"
    #类方法
    @classmethod  #在方法前面加上这行就是类方法
    def add_num(cls):  #cls相当于self， self对象引用，cls类引用，大家规定写的，也可以是别的字母
        cls.num = 100

    #静态方法
    @staticmethod
    def print_menu():  #静态方法（）可以是空的，如果有参数，后面调用也要有参数
        print("----------------------")
        print("    穿越火线V11.1")
        print(" 1. 开始游戏")
        print(" 2. 结束游戏")
        print("----------------------")


game = Game()
#Game.add_num() #可以通过类的名字调用类方法
game.add_num() #还可以通过这个类创建出来的对象去调用这个类方法
print(Game.num)

Game.print_menu() #通过类 去调用静态方法
game.print_menu() #通过实例对象 去调用静态方法

"""
类方法修改类属性，实例方法修改实例属性，
静态方法只是打印简单内容，跟类属性，实例属性都没关系
"""