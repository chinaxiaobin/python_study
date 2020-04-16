f = open("/data/test2.123",mode="w",encoding="utf-8")
f.write("娃哈哈") #本次写的时候,默认先清空,再写入 ,如果多个f.write()则都能写上 所有w w+ wb都是这样
f.write("周杰伦\n")  # \n表示换行
f.flush() #刷新管道,把没写完的写进去 然后执行后面的close
f.close()
