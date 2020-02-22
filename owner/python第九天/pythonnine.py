import time
# 实现带参数的装饰器
def funa(par="hello"):
	def funb(func):
		def fund(*arga,**argb):
			print("%s---%s:%s登录"%(par,func.__name__,time.ctime(time.time())))
			return func(*arga,**argb)
		return fund
	return funb

# 定义被装饰函数
@funa("welcome")
def fune(a):
	print(a)

# 调用函数
fune("lgm")













































































