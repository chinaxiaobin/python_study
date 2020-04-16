f1=open("/tmp/img.jpg",mode="rb")
f2=open("/tmp/img2.jpg",mode="wb")
for line in f1:
    f2.write(line)

