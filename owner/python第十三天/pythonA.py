# Socket套接字
from socket import *

# 创建socket
# upSocket=socket(AF_INET,SOCK_DGRAM)
# 定义对方的地址
# sendAddr=("127.0.0.1",8080)
# 发送数据
# upSocket.sendto(b"hello world",sendAddr)
# 关闭连接
# upSocket.close()

# 发送、接收数据
# 创建socket
upSocket=socket(AF_INET,SOCK_DGRAM)
# 绑定端口号，否则是动态的
bindAddr=("",7788)
upSocket.bind(bindAddr)
# 定义对方的地址
sendAddr=("127.0.0.1",8080)
# 发送数据
upSocket.sendto("你好！".encode("gbk"),sendAddr)
# 接受数据
recData,recAddr=upSocket.recvfrom(1024)
print("从%s接收的数据是：%s"%(recAddr,recData.decode("gbk")))
upSocket.close()





























