# for i in range(1,101):
#     print(f"今天是向小美表白的第{i}天")
#     for j in range(1,11):
#         print(f"送给小美的第{j}朵玫瑰花")
#     print(f"小美，我喜欢你（第{i}天的表白结束）")
#
# print(f"第{i}天，表白成功")

i = 1
while i <=9:
    j = 1
    while j <= i:
        print(f"{i} * {j} = {i * j}",end='\t')
        j += 1
    print()
    i += 1



for i in range(1,10):
    for j in range(1,i + 1):
        print(f"{i} * {j} = {i * j}",end='\t')
    print()

