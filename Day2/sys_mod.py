#Author: kobe
'''
import sys
#print (sys.path)
print (sys.argv)
print(sys.argv[2])
'''

import os
cmd_res = os.system("dir")
cmd_res = os.popen("dir").read()
print("---->" ,cmd_res)

os.mkdir("new_dir2")


