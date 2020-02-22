# 类装饰器
class Test(object):
	def __call__(self):
		print("重写这个方法，此对象就是一个callable对象")

import time
# 定义装饰类
class Log(object):
	def __init__(self,clac):
		print("装饰__init__")
		self.clac=clac

	def __call__(self):
		print("%s返回callable"%time.ctime(time.time()))
		self.clac()

# 定义装饰函数对象
@Log
def func():
	print("旧的功能")

print(type(func))
func()

# 对象池
a=123
b=123
print(id(a),id(b))
a=257
print(id(a))
b=257
print(id(b))

# 查看引用计数
import sys
a=1522
print(sys.getrefcount(a))

# 引用计数gc造成循环引用例子
import gc
class ClassA():
	def __init__(self):
		print('object born,id:%s'%(hex(id(self))))

# 运行f2()，进程占用的内存会不断增大
def f2():
	while True:
		c1=ClassA()
		c2=ClassA()
		c1.t=c2
		c2.t=c1
		# 删除对象
		del c1
		del c2

# 把python的gc关闭
gc.disable()
# f2()

# 测试属性访问拦截器
class School(object):
	def __init__(self,name,age=25):
		self.name=name
		self.age=age
	def __getattribute__(self,obj):
		if obj=="name":
			return "lgm"
		else:
			return object.__getattribute__(self,obj)

s=School("lrx")
s.age=24
print(s.name,s.age)
























# 