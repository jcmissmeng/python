# 协程
import time

def fun1():
	while True:
		print("---A---")
		# 存在yield可认为是一个协程
		yield
		time.sleep(0.5)

def fun2(s):
	while True:
		print("---B---")
		# 协程的切换
		next(s)
		time.sleep(1)

c=fun1()
fun2(c)




































