#变量格式，
#变量名 = 值，等号是赋值运算符
from operator import truediv

num1 = 3
num2 = 4
total = num1 + num2
print(total)
a = 666
#解释器做了两件事1.在内存中创建了一个66的数据 2.创建了一个 变量a，把666保存到a中去
b = a
print(b)
#同一个变量反复赋值，不会报错，会执行print上面的最后一个赋值语句，代码从上到下执行

#2.标识符，程序员定义的变量名、函数名
#不能以数字开头，不能是关键字，只能由字母、数字、下划线组成，严格区分大小写

#3.字符类型，int 任意大小的整数
num = 1
#检测数据类型的方法，type()
print(type(num))
# float 小数
num2 = 1.5
# bool （重点）有固定写法，一个为真一个为假，True False ,首字母必须大写,bool值可以当作整型来对待，True为1，Flase为0；
print(type(True))
print(True + False)
# complex z = a +bj,a是实部，b是虚部，j是虚数单位

#4。字符串类型，需要加上引号，单引号双引号都可以，包含多行内容的时候也可以使用三引号
# name = 'six'
# print(type(name))
# name = """nihao
# wobuhao """
# print(name)

#5.格式化输出，占位符生成一定格式的字符串如%s 字符串（较常用）
# name = 'klh'
# print("我的名字：%s" % name)
#5.1 %d，整数
# age = 18
# print("我的名字：%s,年龄 ：%d" % (name,age))
#5.2浮点数 %f
# a = 1.2
# print("%f" % a)#默认六位小数，遵循四舍五入原则
#%.3f代表设置三位小数
#%%
# print("woshi%%de%%" % ())
#5.3f格式化 格式：f"{表达式}"  ！！！！这个好！！
name = "bb"
age = 18
print(f"我的名字是{name}，我今年{age}岁了" )
