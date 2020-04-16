money = int(input("请输入你这个月的工资:"))
if money <= 1000:
	print("走路回家")
elif 1000 < money < 5000:
	print("打车回家")
else: 
	print("开特斯拉回家")
