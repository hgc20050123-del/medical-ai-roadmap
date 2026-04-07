# for格式：
#for 临时变量 in 可迭代对象:
    #循环体
# str = "1233212"
# for i in str:
#     print(i)

#range()
#用来记录循环次数，相当于一个计数器
# for i in range(1,6):   #包前不包后
#     print(i)
#range里面只写一个数。默认为循环次数，从0开始
#for循环计算1+2+3+...+99+100
# s = 0 
# for i in range(1,101):
#     s += i
# print(s)

#break和continue都是循环中专门使用的关键字
#break是结束所有循环 ， continue是结束当前循环，进入下一个循环
# i = 1
# for i in range(1,6):
#     print(f"我在吃第{i}个苹果")
#     if i == 3:
#         print("我吃饱了")
#         break
#     i += 1


# i = 1
# for i in range(1,6):
#     print(f"我在吃第{i}个苹果")
#     if i == 3:
#         print("这个苹果烂了，不吃了")
#         continue
#     i += 1

# symptoms = ["头痛", "发热", "胸痛", "咳嗽", "乏力"]
# for i in symptoms:
#     print(i)
#     if i == "胸痛":
#         print("您现在情况很危险，请赶快就医")

# 让用户输入症状，多个症状用中文逗号隔开
user_input = input("请输入症状列表（例如：头痛，发热，胸痛，咳嗽）：")

# 转成列表
symptoms = user_input.split("，")

# 遍历输出
for symptom in symptoms:
    symptom = symptom.strip()  # 去掉前后空格
    print("症状：", symptom)

    # 遇到“胸痛”给出重点提示
    if symptom == "胸痛":
        print("⚠ 重点提示：出现胸痛时应重点关注，必要时尽快就医。")