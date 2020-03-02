# UDP广播
from socket import *

upSocket=socket(AF_INET,SOCK_DGRAM)

# 广播设置
upSocket.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
sendAddr=("<broadcast>",7788)

upSocket.sendto(b"hello",sendAddr)

upSocket.close()



































