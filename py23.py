#正则表达式
#字符串处理工具，导入re模块
import re
#语法比较复杂，可读性较差，但是通用性很强适用于多种编程语言
#使用match方法匹配数据，re.match()如果起始位置没有匹配成功，返回none，如果匹配成功可以使用group()提取数据
# re.match(pattern,string,flags)
# pattern是要匹配的正则表达式，string是要匹配的字符串
# res = re.match("bing","bingbingfirst")
# print(res)
# print(res.group())#一开头位置匹配


#高级用法
# res = re.search("bingdd","ingbingddfirst")
# print(res.group())
#
# res = re.findall("bing","ingbingddfbingirst")
# print(res)

# res = re.sub('bing','fuck','bingbingwithme')#替换
# print(res)

# res = re.split("e","he,lk")#分割
# print(res)

#贪婪与非贪婪
# res = re.match("em*",'emmmmm>>')
# print(res.group())

# res = re.match("em*?",'emmmmm>>')
# #print(res.group())



