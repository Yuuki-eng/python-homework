# i = 0
# while i < 100:
#     print("小美。我喜欢你")
#     i += 1

#需求：通过while循环，计算从1加到100的和
#终止条件不要忘记，设置为确保while循环100次
#确保累加的数字，从1开始，到100结束

# sum = 0
# i = 1
# while i <= 100:
#     sum += i
#     i += 1

# print(f"1到100累加的和，{sum}")

import random
num = random.randint(1,100)


#通过一个布尔类型的变量，做循环的标记
# flag = True
# while flag:
#     guess_num = int(input("输入你要猜测的数字:"))
#     if guess_num == num:
#        print("恭喜您就猜中了")
#        flag = False
#     else:
#         if guess_num > num:
#            print("您猜的数字大了")
        # else:
        #    print("您猜的数字小了")


i = 1
j = 1
while i <= 100:
    print(f"今天是第{i}天，准备表白....")

    while j <=10:
        print(f"送给小美第{j}只玫瑰花")
        j += 1

    print("小美，我喜欢你")
    i += 1

print(f"坚持到第{i-1}天，表白成功")
