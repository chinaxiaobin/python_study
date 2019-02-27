class SweetPotato():

    def __init__(self):
        self.CookedString = "生的"
        self.CookedLevel = 0
        self.Condiments = []

    def __str__(self):
        return "地瓜 状态：%s(%d),添加的作料有：%s" %(self.CookedString,self.CookedLevel,str(self.Condiments))

    def cook(self,cooktime):
        self.CookedLevel += cooktime
        if self.CookedLevel >=0 and self.CookedLevel < 3:
            self.CookedString = "生的"
        elif self.CookedLevel >=3 and self.CookedLevel <5:
            self.CookedString = "半生不熟"
        elif self.CookedLevel >= 5 and self.CookedLevel <8:
            self.CookedString = "熟的"
        else:
            self.CookedString = "考糊了"

    def addCondiments(self,item):
        self.Condiments.append(item)


#创建对象

di_gua =  SweetPotato()

di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.addCondiments("大蒜")
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.addCondiments("番茄酱")
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.addCondiments("孜然")
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.addCondiments("芥末")
print(di_gua)
di_gua.cook(1)
print(di_gua)
