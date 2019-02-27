class Base(object):
    def test(self):
        print("--Base")
class A(Base):
    def test(self):
        print("--A")
class B(Base):
    def test(self):
        print("---B")
class C(A,B):
    def test(self):
        print("--C")

c = C()
c.test()

print(C.__mro__)  #如果有多个test方法，默认调取自己的方法，如果自己的类中没有就调取父类中的，具体
#调取顺序   类名.__mro__