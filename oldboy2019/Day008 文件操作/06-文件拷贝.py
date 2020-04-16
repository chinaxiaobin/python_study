f1 = open("/data/test.jpg",mode="rb")
f2 = open("/data/test2.jpg",mode="wb")
for line in f1:
    f2.write(line)

#f2.write(f1.read())  #不要用这个,要用上面那个一行行读,不然文件大就挂了电脑

f1.close()
f2.flush()
f2.close()


