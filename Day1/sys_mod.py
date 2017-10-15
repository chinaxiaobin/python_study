'''
Day2-1-2-3


import sys
print(sys.path)
#打印环境变量,结合cmd进入D:/project测试
#打印的路径是python调用库和某些模块的路径位置
#'D:\\Program Files (x86)\\python3.6\\lib\ #就是标准库存在的位置
#'D:\\Program Files (x86)\\python3.6\\lib\\site-packages'] # site-packages就是第三方库存在的位置




print(sys.argv) #打印相对路径和cmd测试
print(sys.argv[2])
#cmd中测试
#cd  d:/project
#python  sys_mod.py  1 2 3
#['sys_mod.py', '1', '2', '3']
#print(sys.argv[2])

##########################################################

1.
import os  #与操作系统交互，创建目录，查看大小，文件数量
print(os.system("dir"))

2.
import os
cmd_res = os.system("dir")
print("--->" ,cmd_res)
#cmd_res = os.system("dir")  #这里赋值的是状态码，执行命令不保存结果

3.
就想存结果，怎么存，os.system("dir")只执行命令在屏幕，不保存结果

cmd_res = os.popen("dir").read() #这个可以赋值结果，先存到内存中，然后通过read取回结果
print("---",cmd_res)

4.

os.mkdir("new_dir") #创建目录
'''

import login  #调用第三方模块，我们自己创建的，需要在当前目录下，或在site-packages目录下
               #或者加入我们自己的路径

#Day2-4

#pyc是什么东西？
'''
python是解释型语言，解释一句执行一句

编译型语言执行之前编译成机器语言，然后与cpu交互运行，非常快，典型例子C语言

java先编译成字节码，然后运行时通过解释器解释成机器文件

python可以说成是先编译后解释的语言，编译我们看不到而已
当python程序运行时，编译的结果则是保存在位于内存中的PyCodeObject中，当Python
程序运行结束时，Python的解释器则将PyCodeObject写回到pyc文件中
当python第二次运行时，首先程序会在硬盘中寻找pyc文件，然后检测时间和源文件哪个最新，是否被更改过，
如果找到则直接载入，如果源代码最新，则先执行源代码，没有则重复上面的步骤
所以说pyc是PyCodeObject的一种持久化保存方案，
'''

