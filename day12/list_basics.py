# #4.列表
# 基本格式：
# 列表名 = [元素1，元素2，元素3]
# 注意：元素之间的数据类型可以各不相同
# li = [1,23,312,4]
# print(li)
# print(li[3])
# print(li[0:3])
# for i in li:     列表是可迭代对象，可以for循环遍历输出
#     print(i)

#5.列表常见操作
#5.1 添加元素
#  append()  extend()  insert()
# li.append("3232")   #整体直接加入
# li.extend("hgc")    #分散添加
# li.insert(2,2005)   #在指定位置加入元素，如果有元素，原有元素就会后
# print(li)


# 5.2 修改元素
#直接通过下标就可以修改
# li[2] = "g"
# print(li)

#5.3 查找元素
#in： 判断指定元素是否存在列表中，如果存在就返回Ture，不存在就返回Flase
#not in ： 判断指定元素是否存在列表中，如果不存在就返回Ture，存在就返回Flase

# 5.4 删除元素
#  del
# del li[3]
# print(li)

# pop:删除指定下标数据python3版本默认删除最后一个元素

#remove  根据元素的值进行删除
# li.remove("aaa")   #默认删除最开始出现的元素
# print(li)

#5.5排序 
# sort：将列表从小到大的顺序排序
# li.sort()
# print(li)
#reverse：倒序，将列表倒置
# li.reverse()
# print(li)

#5.6 列表推导式
#格式一：[表达式 for 变量  i 列表]
# li = []
# [li.append(i) for i in range(1,6)]
# print(li)

#5.7 列表嵌套
#一个列表里面含有一个列表
# li = [1,33,2,[3,3,32,]]
# print(li[3])

patient_list = ["张三","李四","王五","张李六"]
patient_list.append("老王")
patient_list.remove("王五")
patient_list[2] = "零四"
for i in patient_list:
    print(i)