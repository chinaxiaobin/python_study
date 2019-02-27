class Dog():
    pass

dog1 = Dog()
dog2 = dog1
import sys
count = sys.getrefcount(dog1)
# 默认要减1，因为getrefcount在计算引用计数的时候，会自身创建一个来计数
print(count)