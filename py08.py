# 1.深浅拷贝
# li = [1,2,3]
# print(li)
# li2 = li
# print(li2)
# #新增元素
# li.append(4)
# print(li)
# print(li2)
#复制等于完全共享资源，一个值的改变，会完全被另一个值共享，随着源对象一起变化

# # 2.2浅拷贝，数据半共享
# #会创建新的对象，拷贝第一层的数据，嵌套曾会指向原来的内存地址
# import copy #导入copy模块
# li = [1,2,3,[4,5,6]]#定义一个嵌套列表
# li2 = copy.copy(li)
# print(li)
# print(li2)
# print("li内存地址：",id(li))
# print("li2内存地址：",id(li2))
# #内存地址不一样说明不是同一个对象
# #嵌套列表增加元素
# li[3].append(7)
# print(li)
# print(li2)
# #说明li和li2的嵌套列表的内存地址是一样的

#2.3深拷贝，数据完全不共享
import copy
li = [1, 2, 3]
li2 = copy.deepcopy(li)
print(li)
print(li2)
#深拷贝即使是给嵌套列表增加元素li2也不会增加元素，因为嵌套元素的地址也是不一样的，是完全独立于li的