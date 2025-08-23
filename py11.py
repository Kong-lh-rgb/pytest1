#闭包和修饰器
#1.递归函数
#2.闭包
#条件：1.嵌套函数 2.内层函数使用外层函数的局部变量 3.外层函数的返回值是内层函数的函数名
def outer():
    n = 10
    def inner():
        print(n)
    return inner
# print(outer())
ot = outer()#调用外函数
ot()#调用内函数

#3.装饰器