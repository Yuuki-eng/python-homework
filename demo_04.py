# i = 1
# while i <= 9:
#    j = 1
#    while j <= i:
#
#        print(f"{j} * {i} = {j * i}\t",end='')
#        j += 1
#
#    i += 1
#    print()

# 1. 计数可以在循环外定义一个整数类型变量用来做累加计数
count = 0
for i in range(10):
    count += 1
print(count)

# 2. 判断是否为字母"a"，可以通过if语句结合比较运算符来完成
char = 'a'
if char == 'a':
    print("是字母a")
else:
    print("不是字母a")