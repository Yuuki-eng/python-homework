# print(type("21"))
# print(type(21))
# print(type(12.12))

#第一种——分钟转换为小时
#def 先定义一个函数，加上一个公式，可以得到最后的结果
# def minute_to_hour(minutes):
#     return minutes * 60
# result = minute_to_hour(5)
# print(result)


#第二种——小时转换为分钟
#int(input())  输入函数
# hour = int(input())
# #调用函数
# minute = hour * 60
# print(minute)

def different_max_to_min(list_nums):
    if list_nums:
        max_num = max(list_nums)
        min_num = min(list_nums)
    else:
        return 0
numbers = list(map(int,input().split()))

print(different_max_to_min(numbers))