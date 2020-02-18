# 命令行python或ipython中，重新加载模块
# from imp import *
# reload(模块名)

# a="hello world"
# b="hello world"
# print(a==b,a is b,id(a),id(b))
# a=78986565665465
# b=78986565665465
# print(a==b,a is b,id(a),id(b))
# a=[15645146,"sdfsd",[1]]
# b=[15645146,"sdfsd",[1]]
# print(a==b,a is b,id(a),id(b))

# 浅拷贝
# import copy
# c=a[:]
# print(a==c,a is c,id(a),id(c))
# c=list(a)
# print(a==c,a is c,id(a),id(c))
# c=copy.copy(a)
# print(a==c,a is c,id(a),id(c))
# a[-1].append(2)
# print(c)

# 深拷贝
# d=copy.deepcopy(a)
# a[-1].append("str")
# print(a,d)

# property的用法（装饰器）
class Person(object):
	def __init__(self,name):
		self.__name=name

	# def setName(self,name):
	# 	self.__name=name

	# def getName(self):
	# 	return self.__name
	# 	
	# # 装饰函数，简化set和get用法
	# name=property(getName,setName)
	
	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self,name):
		self.__name=name


p=Person("lrx")
print(p.name)
p.name="lgm"
print(p.name)

# 生成器
# 简单创建方式
G=(x*2 for x in range(5))
print(next(G),next(G))

def fie(n):
	i=0
	a,b=1,1
	while i<n:
		# 放弃CPU控制权，函数暂停在这里，下次再用时从这里继续执行
		yield b
		a,b=b,a+b
	return "Done"
f=fie(10)
print(type(f),next(f),next(f))

def fiee():
	i=0
	b=0
	while i<5:
		# 放弃CPU控制权，函数暂停在这里，下次再用时从这里继续执行
		temp=yield b
		print(temp)
		print(i)
		i+=1
	return "Done"

f=fiee()
next(f) 
next(f) # 等价于f.send(None)
f.send("hah")

# from collections import Iterable
# print(isinstance([],Iterable))

# from collections import Iterator
# print(isinstance([],Iterator))
# # 可用next方法
# print(isinstance(iter([1,2]),Iterator))

# 打印全局变量和局部变量
# print(globals())
# print(locals())

# 闭包（三个条件）
# 模拟一元一次方程
def outf(a,b):
	def inf(x):
		# print(m,n)
		return a*x+b
	return inf

f=outf(2,4)
print(f(3),f(4))

# 装饰器
def w1(funf):
	def inner():
		print("hello",end=" ")
		funf()
	return inner
# 装饰器第一种调用
@w1
def funs():
	print("旧世界")

funs()
# 装饰器第二种调用
def funt():
	print("新世界")
f=w1(funt)
f()

# 通用装饰器
import time
def aaa(bbb):
	def ccc(*d,**e):
		print("%s----%s"%(time.time(),bbb.__name__))
		bbb(*d,**e)
	return ccc

def fff(ooo):
	print(ooo)

print(aaa(fff("hello world!")))






