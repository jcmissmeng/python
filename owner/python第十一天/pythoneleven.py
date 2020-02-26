# 多进程
from multiprocessing import Process,Pool
import time,os,random

# 测试进程间通信,使用全局变量是不可以进行进程间通信的
num=100

# 创建多进程方式一：继承Process类
class SubProcess(Process):
	def __init__(self,interval):
		Process.__init__(self)
		self.interval=interval

	# 重写run方法
	def run(self):
		global num
		print("%s子进程开始"%os.getpid())
		num+=100
		tStart=time.time()
		time.sleep(self.interval)
		tEnd=time.time()
		print("%s子进程已结束，花费了%s秒,num=%s"%(os.getpid(),tEnd-tStart,num))

if __name__=="__main__":
	print("%s主进程开始"%os.getpid())
	tStart=time.time()
	p=SubProcess(2)
	p.start()
	p.join()
	tEnd=time.time()
	print("%s主进程结束，花费了%s秒,num=%s"%(os.getpid(),tEnd-tStart,num))

# 进程池
def worker(msg):
	print("%s子进程开始，msg:%s"%(os.getpid(),msg))
	tStart=time.time()
	time.sleep(random.random()*2)
	tEnd=time.time()
	print("%s子进程已结束，花费了%s秒"%(os.getpid(),tEnd-tStart))

# if __name__=="__main__":
# 	print("%s主进程开始"%os.getpid())
# 	po=Pool(3)
# 	for i in range(5):
# 		po.apply_async(worker,(i,))
# 	po.close()
# 	po.join()
# 	print("%s子进程已结束"%os.getpid())



































