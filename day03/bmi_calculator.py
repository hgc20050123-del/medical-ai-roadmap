# 3.数值类型
# 3.1  int整型（常用）：任意大小的整数,如：-1，0，1，100，-100  
num = 1
# 检测数据类型的方法：type()
print(type(num))
# 3.2  float浮点型（常用）：小数，如：1.0，-1.0，3.14
num = 1.7
print(type(num))
# 3.3  bool布尔型（常用）：一个为True(真)，另一个为False(假
print(type(True))
print(type(False))
#bool值可以当作整型来对待，True的值为1，False的值为0
print(True + False) # 输出1
#3.4 complex复数类型：实数和虚数的组合，比如1 + 2j
a = 1 +2j  #固定格式：实数部分 + 虚数部分j，虚数单位只能是j，不能是i
print(a)
#可以相加
#4. 字符串str类型（常用）：由一个或多个字符组成的文本，如："Hello, World!"，'Python'
name = "hgc"
print(type(name))
name = """hgc
hhh"""
print(name)
"""我是注释
我可以换行
哈哈哈"""
#多行注释和用三引号的字符串的区别：多行注释不会被当作字符串处理，而三引号的字符串会被当作一个字符串对象处理，可以赋值给变量或者打印输出。
#5.格式化输出
#格式化输出：使用占位符%来表示要输出的变量的位置和类型
# 5.1  %s：字符串占位符
name = "hgc"
print("我的名字是%s" % name)
print("我的名字是name") # 这种方式会把name当作普通字符串输出，而不是变量的值
name = "yyx"
print("我对象的名字是%s" %  name )
# 5.2 %d:整数占位符
weight = 70 
height = 170 
age = 21
print("我的体重是%d公斤, 我的身高是%d厘米 ,我的年龄是%d岁" % (weight,height,age))
print("我的名字是%s,我的体重是%d公斤" %(name,weight))
# %4d：表示输出的整数至少占四个字符宽度，如果整数不足四位，则在左侧补空格；如果整数超过四位，则正常输出。
num = 123456
print("%4d" % num) # 输出123456
num = 123
print("%4d" % num)  # 输出 123（前面有一个空格）
print("%2d" % num) #  原样输出123
print("%06d" % num) # 输出00123（前面补0）  
# 5.3 %f:浮点数占位符（常用，默认保留6位小数）
pi = 3.14159265
print("%f" % pi) # 输出3.141593,四舍五入保留6位小数
# %.4f:表示输出的浮点数保留4位小数，超过4位的小数部分会被四舍五入。
print("%.4f" % pi) # 输出3.1416 
print("%.2f" % pi) # 输出3.14
# 5.4 %%:表示输出一个百分号%
print("我是%%,你是%%" % ()) # 输出：我是%,你是% 
# 5.5  f-string格式化字符串（常用）：在字符串前加f或F，使用{}来包含要输出的变量或表达式
name =  "hgv"
age = 22
print(f"我的名字是{name},我的年龄是{age}岁")
weight = 100
print(f"我的体重是{weight}公斤")   #输出：我的体重是100公斤
weight = 70 
height = 1.7
BMI = weight/(height**2)
print(f"我的BMI指数是{BMI:.2f}")