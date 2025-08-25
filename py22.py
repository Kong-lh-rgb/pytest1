#协程
#Y应用场景，如果一个线程里i/o操作比较多的时候，用协程
#适合高并发处理
# py中使用一个第三方模块greenlet进行封装，使得切换任务变得更加简单
# 打开Python解释器验证
# import greenlet
# print(greenlet.__version__)  # 应该输出 3.1.1
#1.实现任务切换通过greenlet
# from greenlet import greenlet
# def sing():
#     print("sing")
#     # g2.switch()实现协程的切换
#     print("over")
# def dance():
#     print("dance")
#     print("over")
# # sing()
# # dance()
# if __name__=="__main__":
#     g1 = greenlet(sing)
#     g2 = greenlet(dance)
#     g1.switch()
#     g2.switch()

#更强大的模块gevent实现自动的切换遇到i/o操作会自动切换，属于主动切换
#使用
import gevent
import time
# gevent.spawn(函数名)创建协程对象
# gevent.sleep()耗时操作
# gevent.join()阻塞等待某个对象结束
# gevent.joinall()等待所有结束
def sing():
    print(1)
    gevent.sleep(2)
    print(2)
def dan():
    print(3)
    time.sleep(3)
    print(4)
if __name__=="__main__":
    g1 = gevent.spawn(sing)
    g2 = gevent.spawn(dan)

    g1.join()
