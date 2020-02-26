# 多线程
from threading import Thread
import time,threading

def saysome(msg):
	print("子线程开始")
	time.sleep(1)
	print("子线程结束")

if __name__=="__main__":
	ls=[]
	for i in range(3):
		t=Thread(target=saysome,args=(i,))
		t.start()
		ls.append(t)

	# 查看当前线程的数量
	print("当前线程的数量是：%s"%len(threading.enumerate()))

	# 使主线程等待
	for i in ls:
		i.join()

	print("主线程结束")































