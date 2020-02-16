def pline():
	print("-"*30)
pline()

# 打开文件，w：没有文件新建文件
# f=open("1.txt","w")
# print(f)
# f.close()

# 写文件
# f=open("1.txt","wt")
# s="hello world"
# f.write(s)
# f.close()

# 读文件
# f=open("1.txt","rt")
# read方法读取长度为Size的字符数，当Size=-1时，读取全部
# s=f.read(-1)
# print(s)
# f.close()
# pline()

# 追加
# f=open("1.txt","at")
# for i in range(1,3):
# 	# 写多行(第一种方式)
# 	f.write("hello world\n")
# f.close()

# 读多行（第一种方式）
# f=open("1.txt","rt")
# for each_line in f:
# 	print(each_line)
# f.close()
# 读多行（第二种方式）
# f=open("1.txt","rt")
# while True:
# 	line=f.readline()
# 	print(line)
# 	if line=="":
# 		break
# f.close()

# 写多行
# f=open("1.txt","wt")
# l=["aa\n","bb\n","cc\n"]
# f.writelines(l)
# f.close()
# pline()

# 此方法在命令行执行
# import sys
# if len(sys.argv) >= 2:
# 	print(sys.argv)
# 命令行输入：python C:\Users\JC\Desktop\学习\python\python第四天\pythonfour.py 1.txt 2.txt
# 执行输出：['C:\\Users\\JC\\Desktop\\学习\\python\\python第四天\\pythonfour.py', '1.txt', '2.txt']
# 拷贝
# f=open(sys.argv[1],"rt")
# s=f.read(-1)
# f.close()
# print(s)
# f=open(sys.argv[2],"wt")
# f.write(s)
# f.close()
# 命令行输入python 绝对路径\pythonfour.py 绝对路径\1.txt 绝对路径\2.txt
# pline()

# 定位
# f=open("1.txt","rb")
# print(f.readline())
# print(f.tell())
# 移动定位,文件打开一定要使用二进制格式
# seek(cookie,whence=()):cookie代表偏移量，whence三个取值：0-文件开始，1-当前位置，2-文件末尾
# f.seek(-3,2)
# print(f.readline())
# f.close()
# pline()

# 操作目录
# import os
# 获取当前路径
# print(os.getcwd())
# 创建目录
# os.mkdir("new")
# 文件重命名
# os.rename("new","old")
# 删除目录,只能删除空目录（遇到拒绝访问）
# os.remove("new")
# 进入目录
# os.chdir("new")
# print(os.getcwd())
# 返回上一级
# os.chdir("..")
# import shutil
# 删除目录，级联删除
# shutil.rmtree("new")
# 列出当前目录
# ll=os.listdir()
# print(ll)

# import os.path
# 是否是文件
# print(os.path.isfile(ll[0]))
# 是否是目录
# print(os.path.isdir(ll[0]))

import myutils
# 列出指定路径下文件目录
myutils.lisdir("C:\\Users\\JC\\Desktop\\学习\\python",1,(1,))
