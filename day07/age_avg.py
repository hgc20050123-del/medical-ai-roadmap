#1.while循环
# 1.1基础语法  
# while 条件：
#     循环体
#     改变变量
# i = 1
# while i <= 10:
#     print("我是帅哥")
#     i += 1 
# 1.2 死循环：
# while True:
#     print("喜喜")

#1.3while循环运用
# 计算：1+2+3+...+100的和
# i = 1
# s = 0
# while i <= 100:
#     s += i
#     i += 1 
# print(s)

# #计算1*2*3....*100
# i = 1
# s = 1
# while i <= 100:
#     s *= i
#     i += 1
# print(s)

# while 循环嵌套
# while 条件1：
#     循环体1
#     while 条件2：
#         循环体2
#         改变变量2
#     改变变量1

# i = 1
# while i <=2:
#     print(f"这是第{i}次外循环")
#     b = 1
#     while b <= 5:
#         print(f"这是第{b}次内循环")
#         b += 1
#     i += 1


# #打印九九乘法表
# a = 1
# while a <= 9:
#     b = 1
#     while b <= a:
#         print(f"{a}*{b}={a*b}",end="\t")
#         b += 1
#     print()
#     a += 1

nums = [36.2,37.2,38.5,37.4,36.8]
total = 0  #总和
count = 0   #元素个数
i  =0      #索引，从0开始
while i < len(nums):  #遍历整个列表
    total += nums[i]   #累加每个元素
    count += 1         #计数+1 
    i += 1 

average = total / count 
print (average)