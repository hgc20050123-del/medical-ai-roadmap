#1.if-else 
#基本格式： 
#if 条件：
    #满足条件输出的代码
#else：   else后面不用加任何条件
    #不满足条件输出的代码
# a = 7
# if a== 666:
#     print("真厉害")
# else:
#     print("还要加油")
#三目运算
#格式： 真结果 if 判断条件 else 假结果
# a = 7
# print("你真棒") if a == 6 else print("还要加油")

#2.if-elif
# score = 77
# if score == 85:
#     print("你的分数是85")
# elif score != 85:
#     print ("你的分数不是八十五")

#3. if嵌套
# 格式: 
# if 条件:
#     满足条件做的事
#     if 条件：
#         满足条件做的事
# ticket = True
# temp = 38
# if ticket == True:
#     print("你可以进站")
#     if 36.0 <= temp <= 37.2:
#         print("你可以上车")
#     elif temp > 37.2:
#         print("你需要隔离")
# else:
#     print("你不可以上车")


# SP = float(input("请输入测得的收缩压："))
# DP = float(input("请输入测得的舒张压："))
#  if SP < 120 and DP < 80:
#      print("你的血压正常")
#  elif 120 <= SP < 139 or 80 <= DP <= 89:
#      print("你的血压偏高")
#  elif SP >= 140 or DP >= 90:
#      print("你是高血压")
#  else :
#      print("输入异常")

