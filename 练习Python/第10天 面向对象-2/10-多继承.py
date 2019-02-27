class Base(object):   #python3默认都是继承object，写上object就叫新式类，不写就是经典类，不写默认也继承object
    def test(self):
         print("----Base")
class A(Base):
   def testA(self):
        print("-- A")
class B(Base):
    def testB(self):
        print("--- B")
class C(A,B):  # 可以继承多个类，拥有多个类的方法和属性
    def testC(self):
      print("--C")

c = C()
c.testA()
c.testB()
c.test()

