# while循环
# while 条件:
#     循环体
#     改变变量
# i = 1
# while i <= 3:
#     print("hhxxttxs")
#     i = i + 1

# 循环嵌套
# while 条件1:
#     要做的事情1
#     要做的事情2
#     while 条件2:
#         要做的事情3
#         要做的事情4

# for循环
# 基本格式
# for 临时变量 in 可迭代对象:
#     循环体
# 注意冒号和缩进
# str = "abcde"
# for i in str:
#     print(i)

# range函数 用来记录循环次数，相当于一个计数器
for i in range(1,6):#规则，包前不包后，输出1-5；
    print(i)

#encode和decode进行编码和解码
a = 'hello'
a1 = a.encode()#编码为比特型
a2 = a1.decode()#解码为原来的hello

#字符串拼接
print("10" + '10')
#星号代表重复输出
print("wode"*4)
name = 'bingbing'
print('b' in name)#返回True
print('a' in name)#返回False
#使用not in 所得为反义

#下标 类似于数组 格式字符串名[下标值]
#切片 包前不包后原则 从起始位置到结束位置的前一位
st = 'abcdefghijk'
print(st[0:4])#abcd


#字符换常见操作 查找
#find 检测某个字符串是否在主字符串中如果在就返回子字符串开始位置下标，不在返回-1
#index没找到会报错
# #count()返回某个子字符串在主字符串中出现的次数没有就返回0
# print(name.count('b'))

#startwith判断是否以某个子字符串开头startwith(name.startwith('s',3,5))  endwith相同是否以某个字符串结尾 都返回True或False


