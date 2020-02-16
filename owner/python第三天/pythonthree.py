def pline():
	print("-"*30)

# 冒泡排序
l=[2,25,34,18,65,0,37,55]
# for i in range(0,len(l)-1):
# 	flag=True
# 	for j in range(0,len(l)-i-1):
# 		if l[j]>l[j+1]:
# 			l[j],l[j+1]=l[j+1],l[j]
# 			flag=False
# 	if flag:
# 		break
# print(l,i)
# pline()

import math
# 函数
# def calCircle(r):
# 	return (math.pi*r**2,2*math.pi*r)
# # 调用函数
# a=calCircle(3)
# print("圆的周长：%.2f\n圆的面积：%.2f"%(a[-1],a[0]))
# pline()

# 全局变量和局部变量
a="全局变量"
def testa():
	# 定义a具体什么变量
	# global a
	a="局部变量"
	print(a)
	# 打印局部变量
	# print(locals())
	# 打印全局变量
	# print(globals())
# testa()
# print(a)
# pline()

# 形参和实参测试,传入方法中不是地址
a,b=10,20
# def swap(a,b):
# 	a,b=b,a
# 	print("a=%d,b=%d"%(a,b))
# swap(a,b)
# print("a=%d,b=%d"%(a,b))
# def swap2(a,b):
# 	# 返回的元组
# 	return b,a
# a,b=swap2(a,b)
# print("a=%d,b=%d"%(a,b))
# pline()

# 缺省参数(从后向前)
# def addDef(a,b=10,c=20):
# 	return a+b+c
# print(addDef(5),addDef(5,21),addDef(5,9,8))

# 不定长参数
def changeable(a,*b,**c):
	print(a,b,c)
changeable(1,2,e=4,b=5)
o=("c","a")
e=("a","b")
d={"q":2.0,"p":3.14}
changeable(o,*e,**d)

# 递归函数，计算n！
def factor(n):
	if n==1:
		return n
	return factor(n-1)*n
print(factor(6))
# 斐波拉契数列实现
def get_num(n):
	if n==1 or n==2:
		return 1
	return get_num(n-1) + get_num(n-2)
print(get_num(6))
pline()

# 匿名函数
def funn(a,b,f):
	return f(a,b)
print(funn(10,20,lambda a,b:a+b))
# 排序
def funn2(a,f):
	a.sort(key=f,reverse=True)
	print(a)
c=[{"name":"lgm","age":25},{"name":"lrx","age":26}]
funn2(c,lambda x:x["age"])

# eval函数
f=eval("lambda a,b:a**b")
print(f(10,2))
s=eval("('a','b')")
print(type(s))