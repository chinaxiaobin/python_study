#vim 04-给程序传参数.py
import sys
print(sys.argv)

name = sys.argv[1]

print("热烈欢迎%s的到来"%name)  #中间不要有逗号


#python3 04-给程序传参数.py  老李