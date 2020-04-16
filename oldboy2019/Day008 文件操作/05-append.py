f = open("/data/test2.123",mode="a",encoding="utf-8")
f.write("周杰伦")  #追加写
f.flush()
f.close()