#q.字符串编码
# 本质上就是二进制数据与语言文字的一一对应关系
# 1.2Unicode：所有字符都是两个字节
# 好处：字符与数字转换数字快
# 坏处：占用空间大

# 1.3UTF-8：精准，对不同字符用不同长度表示
# 优点：节省空间
# 缺点：字符与数字转换速度慢，每次都需要计算字符需要用多少个字节


#1.4字符串编码转换
# a = "hgc"
# # print(a,type(a))
# a1 = a.encode()  #编码
# print(a1)   #bytes，以字节为单位处理
# a2 = a1.decode()  #解码
# print(a2)

# st = "这是胡贵成"
# st1 = st.encode("utf-8")
# print(st1)
# st2 = st1.decode("utf-8")
# print(st2)

#2.字符串常见操作
#2.1 + 字符串拼接
# a = 36
# b = 77
# print(a+b)  #113,整型为相加
# a = "36"
# b = "77"
# print(a+b)  #拼接

#2.2 *字符串重复
# print("好好学习，天天\n"*8) #\n为换行
# print("好好学习，天天\t"*8) #\t为空四格

# #2.2成员运算符
# #作用：检查字符串中是否包含了某个字符串
# a = "张三李四"
# print("张三" in a)


#2.3  下标
#从左往右，从0开始
# name = "123456789"
# print(name[2])
# print(name[-2])  #从右往左数，下标从-1开始


#2.4 切片
#语法：[开始位置：结束位置：步长]    包前不包后
#从左往右
# st = "qwertyuio"
# # print(st[0:3])  #qwe
# # print(st[4:8])  #tyui
# # print(st[3:])   #rtyuio  下标为3之后的全部截取到
# # print(st[:4])   #qwer    下表为4之前全部截取到
# #从右往左
# print(st[-1:])
# print(st[-1::-1])
# #步长：表示选取间隔，不写步长，默认为1
# #步长的绝对值大小决定切取的间隔，正负号决定切取方向
# print(st[-1:-6:-2])

a = "胡贵成  ai  杨宇轩"
print(a)
#1.去空格
no_space = a.replace(" ","") 
print(no_space) 
#2.转大写
b = a.upper()
print(b)
#3.统计长度
c = len(a)
d = len(no_space)
print(c)
print(d)
#4.替换关键字
e = a.replace("ai","爱").replace(" ","")
print(e)