##age = 20

##print(f"今年我已经{age}岁了")
##if age >= 18:
##print("我已经成年了")     ##true
##  print("即将步入大学生活")  ##false

##print("时间过的真快啊")

##通过input语句，获得键盘输入，为变量age赋值（注意转换成数字类型）
##通过if判断是否为成年人，满足条件则输出提示信息，如下

##print("欢迎来到黑马儿童游乐园，儿童免费，成人收费")
##age = int(input("请输入你的年龄："))

##if age >= 18:
    ##print("您已成年，游玩需要补票10元：")
##else:
    ##print("您未成年，可以免费游玩")
##print("祝您游玩愉快")


##通过input语句获取键盘输入的身高
##判断身高是否超过120cm，并通过print给出提示信息

##print("欢迎来到黑马动物园")
##height = int(input("请输入你的身高："))
##if height >= 120:
    ##print("您的身高超过120cm,游玩需要购票10元")
##else:
    ##print("您的身高未超过120cm,可以免费游玩")
##print("祝您游玩愉快")


cm = int(input("请输入你的身高："))
vip_level = int(input("请输入你的VIP等级（1——10）："))
day = int(input("请告诉我今天几号："))
if cm < 120:
    print("身高小于120，可以免费：")
elif vip_level <= 4:
    print("VIP级别小于4：需要花费5元")
elif vip_level <= 8:
    print("VIP级别小于8，需要花费1元")
elif vip_level > 8:
    print("VIP级别大于8，可以免费游玩")
elif day == 1:
    print("今天为1号免费日，可以免费")
elif day != 1:
    print("今天是普通日，正常购票")
else:
    print("不好意思,条件不满足，需要购票10元")
print("祝你游玩愉快 ")


