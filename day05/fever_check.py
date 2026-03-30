# 1.if判断  格式： if 条件:
#                    满足条件执行的代码
# age = 17
# if age <18:
#     print("你是未成年人")
# score = input("请输入你的分数：")
# if score == "100":
#     print("你真棒")
# if score == "60":
#     print("你还需要加油噢！")
#2.比较运算符： > < >= <= == !=
#== 判断是否相等，相等就返回True，不相等就返回False
#!= 判断是否不相等，不相等就返回True，相等就返回False
# a = 10
# b = 20
# print(a == b) #输出Fals
# print(a != b) #输出True
# print(a > b) #输出False
# print(a < b) #输出True
#3.逻辑运算符： and or not
# and：当且仅当所有条件都满足时，返回True，否则返回False
# BMI = input("请输入你的BMI指数：")
# BMI = float(BMI)
# if BMI >= 18.5 and BMI < 24:
#     print("你的体重很正常哦！")
# if  BMI < 18.5 or BMI >= 24:
#     print("你的体重不太正常哦！")
# or：当至少有一个条件满足时，返回True，否则返回False
# BMI= 17
# if BMI < 18.5 or BMI >= 24:
#     print("你的体重不太正常哦！")
# not：取反运算符，返回条件的相反结果
# BMI = 22
# if not (BMI >= 18.5 and BMI < 24):
#     print("你的体重不太正常哦！")
temperature = input("请输入你的体温：")
temperature = float(temperature)
if temperature > 36.0 and temperature <= 36.9:
    print("你现在体温是正常状态")
if temperature > 36.9 and temperature <= 37.9:
    print("你现在体温是低热状态")
if temperature > 37.9 and temperature <= 38.9:
    print("你现在体温是中度发热")
if temperature > 38.9 and temperature<= 40.9:
    print("你现在体温是高热状态")