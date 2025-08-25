# import time
# current_time = time.strftime("%Y%m%d %H:%M:%S")
# print(f"当前时间：{current_time}")
# from curses.ascii import isalpha

# def rabbit_count(months):
#     fib = [1,1]
#     if months == 1:
#         return fib[0]
#     if months == 2:
#         return fib
#     for i in range(2,months):
#         next_month = fib[i-1] + fib[i-2]
#         fib.append(next_month)
#     return fib
# n = int(input("输入月份数："))
# a = rabbit_count(n)
# for a,b in enumerate(a,start=1):
#     print(f"{a}月{b}对")

#判断101-200之间有多少个素数，并输出所有素数。
# count = 0
# for i in range(101,201):
#     for j in range(2,int(i**0.5)+1):
#         if i%j == 0:
#             break
#     else:
#         print(f"{i}是素数")
#         count += 1
# print(f"总数为{count}")

#打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
# for i in range(100,1000):
#     a = i%10
#     b = (i//10)%10
#     c = i//100
#     if a*a*a+b*b*b+c*c*c == i:
#         print(i)  //是整数取整 /是浮点数取整

# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
# score = int(input("输入成绩："))
# if score >= 90:
#     print("A")
# elif score >= 80 and score <=90:
#     print("B")
# else:
#     print("C")

# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# !/usr/bin/python3

import string
# def count_characters():
#     # 获取用户输入
#     text = input("请输入一行字符：")
#     # 初始化计数器
#     letters = 0
#     spaces = 0
#     digits = 0
#     others = 0
#     # 遍历字符串中的每个字符
#     for char in text:
#         if char.isalpha():  # 判断是否为英文字母
#             letters += 1
#         elif char.isspace():  # 判断是否为空格
#             spaces += 1
#         elif char.isdigit():  # 判断是否为数字
#             digits += 1
#         else:  # 其他字符
#             others += 1
#     # 输出统计结果
#     print(f"英文字母个数：{letters}")
#     print(f"空格个数：{spaces}")
#     print(f"数字个数：{digits}")
#     print(f"其他字符个数：{others}")
# # 调用函数
# count_characters()

# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控
# a = int(input("input1:"))
# b = int(input("input2:"))
# c = 0
# now = 0
# for i in range(1,b+1):
#     now = now * 10 + a
#     c = c + now
# print(c)

# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
# for i in range(1,1001):
#     c = 0
#     for j in range(1,i):
#         if i % j == 0:
#             c = c + j
#     if i == c:
#         print(f"{i}是完数")

# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
def calculate_ball_movement():
    height = 100  # 初始高度
    total_distance = 0  # 总经过距离

    # 第1次落地
    total_distance += height
    print(f"第1次落地：经过{total_distance}米，反弹高度{height / 2}米")

    # 第2到第10次落地
    for i in range(2, 11):
        # 反弹和下落各一次
        height /= 2  # 反弹高度
        total_distance += height * 2  # 反弹+下落

        print(f"第{i}次落地：经过{total_distance:.2f}米，反弹高度{height:.2f}米")

    return total_distance, height


# 调用函数
total, rebound_height = calculate_ball_movement()
print(f"\n最终结果：")
print(f"第10次落地时，共经过 {total:.2f} 米")
print(f"第10次反弹高度为 {rebound_height:.2f} 米")
