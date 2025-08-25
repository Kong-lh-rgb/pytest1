#线程
import threading#导入线程模块
import time
def sing(name):
    print(f"{name}唱歌")
    time.sleep(2)
    print("over")
def dance():
    print("dance")
    time.sleep(2)
    print("over")
#主程序入口
if __name__ == "__main__":
    t1 = threading.Thread(target=sing,args=('klh',))
    t2 = threading.Thread(target=dance)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    time.sleep(2)
    print("全部结束")