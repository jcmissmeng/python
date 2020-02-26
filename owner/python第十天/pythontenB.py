# 集合
# 	元素特点：无序唯一
# 可变序列：列表，字典，集合

# 定义集合
# 第一种方式
s={1,2,3}
# 第二种方式：列表推导式
s={x for x in range(3,7)}
# 第三种方式：转变列表
s=set([2,3,45,6])
print(type(s))

s1={1,2,3,5,4}
# 集合内建方法
# 求并集
s2=s.union(s1)
# 求交集
s2=s.intersection(s1)
# 求差集
s2=s.difference(s1)
# 求并差集
s2=s.symmetric_difference(s1)
print(s2)

# 测试functools包中的两个函数
import functools

# 测试partial函数
# 	作用：设置函数默认参数
def testPartial(*argA,**argB):
	print(argA,argB)
p=functools.partial(testPartial,1,2,3)
p()
p(4,5,name="lgm")

# 测试wraps函数
# 	作用：消除装饰器副作用，还原函数默认属性
import time
def log(func):
	@functools.wraps(func)
	def templ(*argA,**argB):
		"log.__doc__"
		print("%s %s 调用"%(func.__name__,time.ctime(time.time())))
		return func(*argA,*argB)
	return templ
@log
def testf():
	"不加@functools.wraps就会打印log.__doc__,当前testf.__doc__"
	print("hello world")

print(testf.__doc__)

# 测试md5加密，此加密不可逆
import hashlib
# 获取MD5对象
m=hashlib.md5()
# 加密,参数为字节码
m.update(b"ILLgm")
print(m.hexdigest())








