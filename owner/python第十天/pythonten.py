# 内建函数 map 的使用
# 根据提供的函数对指定的序列做映射
# 一个序列映射
m=map(lambda x:x**2,[1,2,3])

# 两个序列映射
m=map(lambda x,y:x+y,[1,2,3],[4,5,6])

# 定义函数映射
def ysfun(x,y):
	return (x,y)
m=map(ysfun,[1,2,3],["m","t","w"])

# 遍历map
print(type(m))
for i in m:
	print(i,end=" ")
print()

# 内建filter函数
# 以匿名函数过滤
f=filter(lambda x:x%2==0,[1,2,3,4,5,6])

# 以空过滤
f=filter(None,"hello")

print(type(f))
for i in f:
	print(i,end=" ")
print()

# 内建reduce函数
from functools import reduce
# 第三个参数为初始值（可无）
r=reduce(lambda x,y:x+y,[1,2,3,4,5,6],3)

r=reduce(lambda x,y:x+y,["b","c","d"],"a")
# 打印
print(r,type(r))









































































