# # def test(fn): #fn是普通形参
# #     print("登录")
# #     print("注册")
# #     fn()
# # def test2():
# #     print("发消息")
# test(test2)
#
#
#3.装饰器
# #让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象，本质上是一个闭包函数
# #1.2标准版装饰器
# def send():#被修饰的函数
#     print("发送消息")
# # send()
# #闭包的三个条件 1.函数嵌套 2.内函数要使用外函数的局部变量 3.外函数的返回值是内函数的函数名
# def outer(fn):#外函数
#     def inner():#内函数
#         fn()
#         print("wssb")
#     return inner#外函数的返回值是内函数的函数名
# print (outer(send))
# outer(send)()


#4.语法糖
# def outer(fn):
#     def inner():
#         print("登录")
#         fn()
#     return inner
#
# @outer
# def send():
#     print("笑死了我")
# send()

#4.1被装饰的函数有参数的
def outer(fn):
    def inner(name):
        print(f"{name}是inner中的参数")
        fn(name)
    return inner
@outer
def func(name):
    print("这是被装饰的函数")
func('bb')