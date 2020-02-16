# 输出
print("hello world")

# 整型赋值
a=10
print(a)

# 查询类型
b=type(a)
print(b)

# 转十进制
c=int("0b1101",2)
print(c)

# 转八进制
d=oct(10)
print(d)

# 转十六进制
e=hex(16)
print(e)

# 转二进制
f=bin(11)
print(f)

# 空字符串和0均认为false
a=""
b=0
if a or b:
	print("空字符串和0均认为false")

# 空值
a=None

# 打印多个变量
a=10
b=20
print(a,b)

# 三个单引号
print('''hello world''')

# 引入库
#import keyword
# 显示所有关键字
#a=keyword.kwlist

# 格式化输出 %x十六进制 %04d以0补全
print("%.2f %d %s"%(1.2,10,"er"))

# 输入
#a=input()

# 整除，取余，次幂
print(20//15,20%15,2**3)

# 自增,复合运算符
a=1
a+=1

# 逻辑运算符
a=4
b=5
# 都为ture返回后值，均为短路
print(a and b)
# 都为ture返回前值，均为短路
print(a or b)
# 非运算
print(not a)