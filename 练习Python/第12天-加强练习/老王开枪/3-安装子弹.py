class  Person(object):
    """人的类"""
    def __init__(self,name):
        super(Person,self).__init__()
        self.name = name

    def anzhuang_zidan(self,dan_jia_temp,zi_dan_temp):
       """把子弹装到弹夹中"""
        #弹夹.保存子弹（子弹）
        dan_jia_temp.baocun_zidan(zi_dan_temp)



"""
sublime同时修改多个
选中一个-ctrl+d选中下一个....
"""

class Gun(object):
    """枪类"""
    def __init__(self,name):
        super(Gun,self).__init__()
        self.name = name #用来记录枪的类型

class Danjia(object):
    """弹夹类"""
    def __init__(self,max_num):
        super(Danjia,self).__init__()
        self.max_num = max_num #用来记录弹夹的最大容量
        self.zidan_list = [] #用来记录所有的子弹的引用

    def baocun_zidan(self,zi_dan_temp):
        """将这颗子弹保存"""
        self.zidan_list.append(zi_dan_temp)


class Zidan(object,sha_shang_li):
    """子弹类"""
    def __init__(self,arg):
        super(Zidan,self).__init__()
        self.sha_shang_li = sha_shang_li  #这颗子弹的威力






def main():
    """用来控制整个程序的流程"""
    #1.创建老王对象
    laowang = Person("老王")
    #2.创建一个枪对象
    ak47 = Gun("AK47")
    #3.创建一个弹夹对象
    dan_jia = Danjia(20)
    #4.创建一些子弹
    zi_dan = Zidan(10) #表示杀伤力


    #5.老王把子弹安装到弹夹中
    #老王.安装子弹到弹夹中（弹夹、子弹）
    laowang.anzhuang_zidan(dan_jia,zi_dan)
    #谁调用的方法，谁用哪个对象创建出来的，就在这个对象创建方法


    #6.老王把弹夹安装到枪中
    #7.老王拿枪
    #8.创建一个敌人
    #9.老王开枪打敌人
    #老王开枪打敌人

if __name__ == '__main__':
    main()