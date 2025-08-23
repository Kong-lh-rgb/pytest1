#作用域 全局变量和局部变量
#异常抛出 raise
# from logging import exception
#
# # raise Exception("异常抛出")
# def funa():
#     #执行了raise语法后面的语句不会继续执行
#     raise exception("yichang")
#     print("hhhhh")
# funa()
# def funb():
#     a = input("输入密码")
#     if len(a) < 6:
#         raise Exception("长度不足")
#     else: return "密码输入成功"
# # print(funb())
# try:#捕获异常使得后续代码可以继续向下执行
#     print(funb())
# except Exception as e:
#     print(e)
# print("123444")

#3. 模块本质上即使py文件，导入一个模块就是执行py文件
#内置模块
#第三方模块，需要使用下载命令进行下载
#3.1自定义模块 注意命名要遵循标识符规定，也不要与内置模块起冲突

#4.模块的导入
#4.1 import 模块名
#调用模块功能 模块名.功能名
#4.2 from 模块名 import 功能名
#4.3 from ... import * 把模块中的所有内容全部导入

#5. as起别名 import 模块名 as 别名
#5.2 as给功能起别名 from 模块名 import 功能名 as 别名

#6 导入包的时候会先执行init文件，不要再其中编写过多代码 