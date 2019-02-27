class Person(object):
    def __init__(self,name):
        super(Person,self).__init__()
        self.name = name

    def anzhuang_zidan(self,dan_jia_temp,zi_dan_temp):
        dan_jia_temp.baocun_zidan(zi_dan_temp)

    def anzhuang_danjia(self,gun_temp,dan_jia_temp):
        gun_temp.baocun_danjia(dan_jia_temp)

class Gun(object):
    def __init__(self,name):
        super(Gun,self).__init__()
        self.name=name
        self.danjia = None
    def baocun_danjia(self,dan_jia_temp):
        self.danjia= dan_jia_temp

    def __str__(self):
        if self.danjia:
            return "枪的信息为：%s,%s"%(self.name,self.danjia)
        else:
            return "枪的信息为：%s,这把枪中没有弹夹"%(self.name)
class Danjia(object):
    def __init__(self,max_num):
        super(Danjia,self).__init__()
        self.max_num = max_num
        self.zidan_list= []

    def baocun_zidan(self,zi_dan_temp):
        self.zidan_list.append(zi_dan_temp)

    def __str__(self):
        return "弹夹的信息为：%d/%d"%(len(self.zidan_list),self.max_num)
class Zidan(object):
    def __init__(self,sha_shang_li):
        super(Zidan,self).__init__()
        self.sha_shang_li = sha_shang_li

def main():
    """用来控制整个程序的流程"""

    #1. 创建一个老王对象
    laowang = Person("老王")
    #2. 创建一个枪对象
    ak47 = Gun("AK47")
    #3. 创建一个弹夹对象
    dan_jia= Danjia(20)  #能给装子弹的个数
    #4. 创建一些子弹
    for i in range(15):
        zi_dan = Zidan(10) #表示杀伤力
    #5. 创建一个敌人

        #6.老王把子弹安装到弹夹中

        laowang.anzhuang_zidan(dan_jia,zi_dan)
        #7.老王把弹夹安装到枪中
        laowang.anzhuang_danjia(ak47,dan_jia)

    #test测试弹夹的信息
    print(dan_jia)
    #test测试枪的信息
    print(ak47)

    #8.老王拿枪
    #9.老王开枪打敌人



if __name__=='__main__':
    main()