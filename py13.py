#面向对象基础
# class Washer:
#     height = 900
# print(Washer.height)
# Washer.width = 450
# print(Washer.width)
# wa = Washer()
# print(wa)
# wa2 = Washer()
# print(wa2)

#构造函数__init__() 用来做属性的初始化或者赋值操作 在类实例化对象的时候会被自动调用
# class Test:
#     def __init__(self):
#         print("ss")
# te = Test()

#next course is p31 2025.6.12
#3.析构函数__del__() 删除对象的时候解释器会默认调用__del__方法
# class Person:
#     def __init__(self):
#         print("我是init方法")
#     def __del__(self):
#         print("我被销毁")
# p = Person()
# print("这是最后一行")#正常运行不会调用del方法，对象结束执行之后系统自动调用del方法

#4面向对象三大特性 封装 继承 多态
#4.1封装 隐藏对象中一些不希望被外部访问到的属性或者方法 隐藏属性只允许在类的内部使用无法通过对象访问
#隐藏属性在 属性名或者方法的前面 加上两个下划线
# class Person:
#     name = "klh"
#     __age = 29 #隐藏属性
#     def introduce(self):#实例方法
#         print(f"{Person.name}的年龄是{Person.__age}")#在实例方法访隐藏属性
# pr = Person()
# print(pr.name)
# # print(pr.age)#无法访问到age
# print(pr._Person__age)#访问隐藏属性
# pr.introduce()

#4.3 私有属性/方法

#继承 类和类之间转变为父子关系 子类默认继承父类的属性和方法
# class 类名（父类名）：
#     代码块
#单继承
class Person:
    def eat(self):
        print("吃饭")
    def sing(self):
        print("唱歌")
class Girl(Person):
    pass #占位符 代码里不写任何东西会跳过
girl = Girl()
girl.eat()

#p34
#多态 前提继承，重写
#构造函数__init__()初始化对象 __new__()