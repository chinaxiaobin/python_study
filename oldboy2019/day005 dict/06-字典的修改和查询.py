# dic = {"刘能":"王小利","赵四":"刘晓光","王木生":"范伟","谢大脚":"于月仙","李大国":"小鬼"}
# dic["王木生"] = "刘伟"
# print(dic)
#
# dic2 = {"刘能":"大阳哥","赵四":"github","王木生":"汪峰","谢大脚":"冯提莫","王大拿":"赵本山"}
# dic.update(dic2)  #把dic2更新到dic1里面去
# print(dic)


#查询
dic = {"刘能":"大阳哥","赵四":"github","王木生":"汪峰","谢大脚":"冯提莫","王大拿":"赵本山"}

#1. 最直观,直接用key
print(dic["刘能"])
#print(dic["周杰伦"]) #当key不存在 会报错

#2. get方法查询
print(dic.get("赵四"))
print(dic.get("周杰伦")) # 当key不存在会报None

print(dic.get("周杰伦","周杰伦不在这里")) #不存在则执行第二个参数
print(dic.get("谢大脚","周杰伦不在这里")) #存在则不执行第二个参数

# 3. setdefault() 1.新增(先看有没有key,如果有就过,如果没有,执行新增)
#                 2.根据key把值返回



dic = {}
dic["盖伦"] = "德玛西亚之力"
value = dic.setdefault("菲奥娜","无双剑姬") #先去跑setdefault新增,如果有,则跳过,然后查出来,如果没有,则新增,然后查询出来

value2 = dic.setdefault("盖伦","刘伟")
print(value2)

value3 = dic.setdefault("薇恩","坑")
print(value3)
print(dic)

