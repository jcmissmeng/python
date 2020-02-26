# 消息队列
from multiprocessing import Manager,Process,Queue,Pool
import random,os,time

def write(q):
	for i in "ABC":
		q.put(i,True)
		print("%s进程将%s放入消息队列"%(os.getpid(),i))
		time.sleep(random.random())

def read(q):
	while True:
		if not q.empty():
			m=q.get(True)
			print("%s进程获取到消息%s"%(os.getpid(),m))
		else:
			break

# if __name__=="__main__":
# 	q=Queue()
# 	p1=Process(target=write,args=(q,))
# 	p2=Process(target=read,args=(q,))
# 	p1.start()
# 	p1.join()
# 	p2.start()
# 	p2.join()

# 测试进程池间的消息队列，此队列使用multiprocessing.Manager().Queue()
def writer(q):
	for i in "welcome":
		q.put(i)

def reader(q):
	for i in range(q.qsize()):
		item=q.get()
		print("获取进程间的消息是：%s"%item)

if __name__=="__main__":
	q=Manager().Queue()
	p=Pool()
	p.apply(writer,(q,))
	p.apply(reader,(q,))
	p.close()
	p.join()
	print("主进程结束")
















