# ThreadLocal变量
import threading

localSchool=threading.local()

def processStudent():
	stu=localSchool.stu
	print("welcome %s at %s"%(stu,threading.current_thread().name))

def processThread(name):
	localSchool.stu=name
	processStudent()

t1=threading.Thread(target=processThread,args=("lgm",),name="1")
t2=threading.Thread(target=processThread,args=("lrx",),name="2")
t1.start()
t2.start()
t1.join()
t2.join()































