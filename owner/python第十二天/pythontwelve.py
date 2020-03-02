# 多进程
# 继承Thread实现线程
from threading import Thread,Lock
import time

class TestThread(Thread):
	def __init__(self,name,times=1):
		Thread.__init__(self)
		self.name=name
		self.times=times

	def run(self):
		print("%s thread is beginning"%self.name)
		time.sleep(self.times)
		print("%s thread is stop"%self.name)

# 测试继承线程
# if __name__=="__main__":
# 	t=TestThread("lgm")
# 	t.start()
# 	t.join()
# 	print("主线程结束")

# Lock线程加锁
def addSum(name):
	global num
	for i in range(100000):
		# 线程加锁
		flag=lock.acquire(True)
		if flag:
			num+=1
			lock.release()
	print("%s 中num=%s"%(name,num))

lock=Lock()
num=0
t1=Thread(target=addSum,args=("t1",))
t2=Thread(target=addSum,args=("t2",))
t1.start()
t2.start()
t1.join()
t2.join()
print("num=%s"%num)

# 线程死锁情况
class LockThread(Thread):
	def run(self):
		if mutexA.acquire():
			print("甲使用了A锁")
			time.sleep(1)
			if mutexB.acquire():
				print("甲使用了B锁")
				mutexB.release()
			mutexA.release()

class LockThreadB(Thread):
	def run(self):
		if mutexB.acquire():
			print("乙使用了B锁")
			time.sleep(1)
			if mutexA.acquire():
				print("乙使用了A锁")
				mutexA.release()
			mutexB.release()

mutexA=Lock()
mutexB=Lock()
# 此时如果启动以上两个线程死锁



























