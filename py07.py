# #1.元组 只支持查询操作
# #tua = (1,2,3,'a',5)
# # print(type(tua))
#
# #字典
# #字典名 = {健1：值1，健2：值2、、、} 键值对格式保存，键和值之间用冒号隔开，每个键值对之间用逗号隔开 健具有唯一性
# # dic = {'name':'bb','age':18}
# # print(dic)
#
# #字典常见操作 查看
# # dic = {'name':'bb','age':20}
# # print(dic['name'])
# # print(dic.get('name'))
# #修改元素
# # dic['name'] = 'nm'
# # print(dic)
# #新增元素 键名存在就修改，不存在就增加
# # dic['tel'] = 12343
# # print(dic)
# #删除元素
# # del dic#删除整个字典
# # del dic['age']
# # dic.clear()#清空字典里的东西，保留字典
# # pop()删除指定键值对，健不存在就会报错
# # dic.pop('name')
#
# #2.len求长度 返回几对键值对
# dic = {'name':'bb','age':20}
# print(len(dic))
# print(dic.keys())#返回所有键名
# print(dic.values())#返回所有值
# print(dic.items())#元组形式返回键值对
#
# #字典的应用场景使用键值对描述物品信息
#
# #集合 集合名 = {元素1，元素2，元素3}
# s1 = {1,2,3}
# s2 = set()#定义空集合 具有无序性
# print(type(s1))
# #集合添加元素 add添加整体 update分散添加
# s1.add(4)
# s1.update('abdc')
# #删除元素 remove()选择删除的元素，如果集合中有就删除，没有就报错
# s1.remove('abdc')
# print(s1)
# #pop默认删除第一个 更具hash排序的第一个元素
# #discard选择要删除的元素有就删除，没有不进行任何操作
#
# #3.交集和并集
# print(a & b)#返回交集
# print(a | b)#返回并集
#
