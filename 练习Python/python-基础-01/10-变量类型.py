"""
type(age) 查看类型

数字：
    整数类型 int
    浮点型：float

"""
age = input("请输入你的年龄:")  #input获取的所有数据，都当作字符串类型  20-->age-->"20"
age_num = int(age) # 去除了双引号之后的值
if age_num>18:
    print("已成年，可以去网吧嗨皮...")

