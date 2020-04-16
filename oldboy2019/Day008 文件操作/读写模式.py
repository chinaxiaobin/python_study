f = open("菜单",mode="r+",encoding="utf-8")
#  f.write("ab")  #r+直接写,表示在文件的开头写入 写入的是字节,把原来的内容盖上

#  s = f.read(1)
#   print(s)
#   f.write("abbb") # r+模式,如果你执行了读操作,那么写操作的时候,都是写在文件的末尾,和光标没有关系


for  line in f:
    print(line)

f.write("555")

f.close()