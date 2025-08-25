#线程之间共享资源
from threading import Thread, Lock
import time
# li = [] #全局变量
# def wdata():
#     for i in range(5):
#         li.append(i)
#         time.sleep(1)
#         print("写入的数据是：",li)
# def rdata():
#     print("读取的数据是：",li)
# if __name__=="__main__":
#     #创建线程
#     t1 = Thread(target=wdata)
#     t2 = Thread(target=rdata)
#     t1.start()
#     t1.join()
#     t2.start()

#资源竞争
a = 0
b = 1000000
lock = Lock()
def add():
    lock.acquire()
    for i in range(b):
        global a
        a += 1
    print("第一次：",a)
    lock.release()
def add2():
    lock.acquire()
    for i in range(b):
        global a
        a += 1
    print("第二次：",a)
    lock.release()
if __name__=="__main__":
    t1 = Thread(target=add)
    t2 = Thread(target=add2)
    t1.start()
    t2.start()