# 3.字符串常见操作
# 3.1查找
# find：检测某个子字符串是否包含在字符串当中，如果在就返回这个子字符串开始位置的下标，否则就返回-1
#find（子字符串，开始位置下标，结束位置下标）
#开始位置下标可以省略，默认在整个字符串内查找
# name = "huguicheng"
# print(name.find("u"))   #1--第一个u的下标为1
# print(name.find("hu"))  #0--第一个hu的h的下标为0
# print(name.find("u",1,6)) 
# print(name.find("u",3,4))
# print(name.find("c",0,5)) #-1--虽然c的下标是5，但是find遵循包前不包后的原则

#index（）：检测某个子字符串是否包含在字符串当中，如果在就返回这个子字符串开始位置的下标，否则就报错
#index（子字符串，开始位置下标，结束位置下标）
# name = "huguicheng"
# print(name.index("hu"))  #0
# print(name.index("hu",2,3)) #报错，遵循包前不包后

#count（）：返回某个子字符串在整个字符串中出现的次数，，没有就返回0
# #count（子字符串，开始位置下标，结束位置下标）
# print(name.count("u"))   #2
# print(name.count("gg"))  #0 --没有就显示0
# print(name.count("u",3,5))    #遵循包前不包后

 
#3.3判断
#1.startswith（）：是否以某个子字符串开头，是的话就返回Ture，反之返回Flase
# startswith（子字符串，开始位置下标，结束位置下标）
# name = "yangyuxuan"
# print(name.startswith("y"))    #Ture
# print(name.startswith("y",3,5))   #Flase

# #2.endswith（）：是否以某个子字符串结尾，是的话就返回Ture，反之返回Flase
# print(name.endswith("n"))   #Ture

#isupper():检测字符串中所有的字母都是大写
#islower():检测字符串中所有的字母都是小写


#3.2修改元素
#1.replace：替换
#replace（新内容，旧内容，替换次数）
# name = "好好学习，天天学习"
# print(name.replace("学习","玩"))  #好好玩，天天玩
# print(name.replace("学习","玩",1))m  #好好玩，天天学习,默认全部替换

#2.split（）：指定分隔符来切字符串
# name = "好好学习，天天学习"
# print(name.split(","))    #['好好学习，天天学习']--以表格形式返回
# #如果字符串不包含分割内容，就不进行分割
# print(name.split("习",1))

#3.capitalize():第一个字符大写，其他都小写
#4.lower（）：大写字母转为小写
#5.upper（）：小写字母转为大写

# symptom = ["发热","胸疼","咯血","头疼"]
# input_symptom=input("请输入要查找的内容")
# if input_symptom == "发热" or"胸疼" or "咯血":
#     print("文本里面有这些内容")

keywords = ["发热","胸疼","咯血"]
input_symptom={}
symptom = input("请输入症状：")
for keyword in keywords:
    input_symptom[keyword] = keyword in symptom
print(input_symptom)