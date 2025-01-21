##定义一个数字（1-10）随机生成，通过3次猜
##案例要求：数字随机生成
##由3次机会猜测数字，通过3层嵌套判断实现
##每次猜不中会提示猜大了还是猜小了


#1.构建一个随机生成的数字变量
import random
num = random.randint(1,10)


guess_num = int(input("输入你要猜测的数字："))

#2。通过if判断语句进行数字的猜测
if guess_num == num:
    print("恭喜第一次就猜中了")
else:
    if guess_num > num:
        print("你猜的数字大了")
    else:
        print("你猜的数字小了")

    guess_num = int(input("再次输入你要猜测的数字"))

    if guess_num == num:
        print("恭喜第二次猜中了")
    else:
        if guess_num < num:
            print("你猜的数字小了")
        else:
            print("你猜的数字大了")

    guess_num = int(input("再次输入你要猜测的数字"))

    if guess_num == num:
        print("恭喜第三次猜中了")
    else:
        print("三次机会用完了，没有猜中")

