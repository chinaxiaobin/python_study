dic = {"黄日华":"天龙八部","吕颂贤":"笑傲江湖","苏有朋":"倚天屠龙记","六小龄童":"西游记"}
#dic.pop("吕颂贤")  #指定key删除

dic.popitem() #随机删除
print(dic)

del dic["苏有朋"] #删除指定的
dic.clear() #字典的清空