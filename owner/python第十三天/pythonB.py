# 重复接受数据
from socket import *
from threading import Thread

def sendMsg():
	global running
	while running:
		msg=input(">>")
		msg+="\n"
		upSocket.sendto(msg.encode("gbk"),sendAddr)

def recvMsg():
	global running
	while running:
		recData,recAddr=upSocket.recvfrom(1024)
		print("<<%s--%s"%(recAddr,recData.decode("gbk")))
		if recData.decode("gbk").startswith("bye"):
			running=False

if __name__="__main__":
	upSocket=socket(AF_INET,SOCK_DGRAM)
	upSocket.bind("",7788)
	sendAddr=("127.0.0.1",8080)
	running=True
	t1=Thread(target=sendMsg)
	t2=Thread(target=recvMsg)
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	upSocket.close()


































