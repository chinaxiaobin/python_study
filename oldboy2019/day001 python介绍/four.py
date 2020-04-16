#嵌套
print("刘伟家,当当当!!!")
gender = input("你是男的还是女的?")

if gender == "女的":
	age = input("你今年多大了?")
	if int(age) > 40:
		print("对不起,你去隔壁吧!!!")
	else:
		print("请进,太白不在")
	print("激动不已,请进")
else:
	print("滚出去")
