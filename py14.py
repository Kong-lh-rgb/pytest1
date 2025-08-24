#单例模式，节省内存空间，减少不必要的资源浪费
#实现方式 @classmethod 装饰器 重写__new__()方法

#可迭代对象 凡是可以作用于for的都是可迭代对象，凡是可以作用于next的都是迭代器
# from collections.abc import Iterable,Iterator
# name = "bingh"
# print(isinstance(name,Iterable)) #是可迭代对象
# print(isinstance(name,Iterator)) #不是迭代器对象
#
# name2 = iter(name) #将name转换为迭代器对象 所以迭代器对象一定是可迭代对象

#自定义迭代器类
# class MyIterator(object):
#     def __init__(self):
#         self.num=1
#     def __iter__(self ):
#         return self
#     def __next__(self):
#         if self.num==100:
#             raise StopIteration("终止")
#         self.num+=1
#         return self.num
# mi = MyIterator()
# print(next(mi))
# for i in mi:
#     print(i)

#生成器 一边循环一边计算的机制叫做生成器 generator
#生成器表达式
# li = [i*5 for i in range(5)]
# print(li)
# gen = (i*5 for i in range(5))
# print(gen)
# print(next(gen))
# print(next(gen))#遇到yield关键字，挂起函数，在下次再运行这个函数的时候，从挂起点继续执行

def generate_numbers(n):
    for i in range(n):
        yield i

numbers_gen = generate_numbers(10)  # 不会立即创建，按需生成

print(next(numbers_gen))  # 0
print(next(numbers_gen))  # 1
print(next(numbers_gen))  # 2
print(next(numbers_gen))  # 3
print(next(numbers_gen))
print(next(numbers_gen))  # 0
