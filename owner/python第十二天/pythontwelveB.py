# 使用锁定义执行顺序	ESC退出
from threading import Thread,Lock
import time


class Thread1(Thread):
	def run(self):
		while True:
			if lock1.acquire():
				print("线程1执行")
				time.sleep(0.5)
				lock2.release()

class Thread2(Thread):
	def run(self):
		while True:
			if lock2.acquire():
				print("线程2执行")
				time.sleep(0.5)
				lock3.release()
				
class Thread3(Thread):
	def run(self):
		while True:
			if lock3.acquire():
				print("线程3执行")
				time.sleep(0.5)
				lock1.release()
				
lock1=Lock()
lock2=Lock()
lock2.acquire()
lock3=Lock()
lock3.acquire()

t1=Thread1()
t2=Thread2()
t3=Thread3()

t1.start()
t2.start()
t3.start()














