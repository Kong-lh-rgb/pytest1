#列表
# li = [1,2,3,4]
# print(type(li))
# print(li[0:3])
#列表的常见操作
# li = ['en', 'jp']
# li.append('df')#整体添加
# li.extend('four')#分散添加
# li.insert(3,'bb')
# print(li)

#修改元素通过下标
# li = [1,2,3]
# li[2] = 'a'
# print(li)
#
#in和not in判断元素是否存在于列表中

# 删除元素 del pop remove
# li =[1,2,3,4]
# del li[0]
#li.pop()#默认删除最后一个元素，根据下标进行删除
#remove根据元素的值进行删除 默认删除第一个找到的元素
# li.remove(1)
# print(li)

#排序 sort当列表按特定顺序排序，默认从大到小
# li = [1,5,2,3,6,4]
# li.sort()
# li.reverse()#倒序排列
# print(li)

#列表推导式 格式[表达式 for 变量 in 列表]  in后面不仅可以放列表还可以放range函数
# li = [1,2,3,4,5,6]
# [print(i) for i in li]

#格式2 [表达式 for 变量 in 列表 if 条件]
#把奇数放进列表里面
# li =[]
# # for i in range(1,6):
# #     if i % 2 == 1:
# #         li.append(i)
# # print(li)
#
# [li.append(i) for i in range(10) if i % 2 == 1]
# print(li)

#列表嵌套
li = [1,2,3,[4,5,6]]