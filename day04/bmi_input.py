#算数运算符 +-*/
print(1+1)
print(1-1)
print(2*6)
print(8/4)
a = 4+3
print(type(a))
# //取整除，结果为整数，向下取整
print(90//13)
# %取余数
print(90%13)
# **幂运算
print(2**3)
print(7.0/2) #使用算数运算符时，如果有一个操作数是浮点数，那么结果也是浮点数
#2.赋值运算符
a = 10
b =  20
n1 = a
n2 = b
print(n1,n2)
# 3. += 复合赋值运算符
a  = 10
a  +=5 #相当于 a = a + 5
print(a)
# 4.比较运算符
print(10 > 5) #True
print(10 < 5) #False
print(10 == 10) #True  
# 赋值运算符只针对变量存在，纯数字使用会出现语法错误
# input()函数获取用户输入，返回值为字符串类型
# name = input("请输入你的名字：")
# print("你好，"+name)
# # 转义字符
#4.1 \t 制表符 通常表示4个空格 ，可以用来对齐文本
print("姓名\t年龄\t性别")
#4.2 \n 换行符
print("第一行\n第二行")
#4.3  \r 回车符 将光标移动到当前行的开头，覆盖之前的内容
print("Hello\rWorld") #输出结果为 Worldo    
#4.4 \\ 反斜杠 用于表示一个普通的反斜杠字符
print("这是一个反斜杠：\\")
#  raw字符串，原始字符串，字符串前加r，表示字符串中的转义字符不进行转义
print(r"这是一个反斜杠：\\") #输出结果为 这是一个反斜杠：\\
weight = float(input("请输入你的体重（kg）："))
height = float(input("请输入你的身高（m）："))
BMI = weight / (height ** 2)
print(f"你的BMI指数为：{BMI:.2f}")