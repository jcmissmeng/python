# 字符串输出多次
# print("="*15)

# input在Sublime中不能使用
#password=input("请输入密码：")
password="213"
# if-elif-else练习
# if password=="213":
# 	print("欢迎a")
# elif password=="258":
# 	print("欢迎b")
# else:
# 	print("密码输入错误")

# 条件语句嵌套
a=1
b=2
# if a==1:
# 	if b==2:
# 		print(a,b)
# 	else:
# 		print(b)
# else:
# 	print(a)

# while循环及for循环实现1加到100
a=1
su=0
# while a<=100:
# 	su+=a
# 	a+=1
# print("whileSum=%s"%su)

su=0
# range(始，终，间隔)取范围，前闭后开
# for b in range(1,101):
# 	su+=b
# print("forSum=%s"%su)

# for打印序列
# for c in "hello":
# 	print(c,end=" ")
# print()

# 实现九九乘法表
i=1
# while i<=9:
# 	j=1
# 	while j<=i:
# 		print("%d*%d=%d"%(i,j,i*j),end=" ")
# 		j+=1
# 	print()
# 	i+=1

# for i in range(1,10):
# 	for j in range(1,i+1):
# 		print("%d*%d=%d"%(i,j,i*j),end=" ")
# 	print()

# 序列之字符序列
str="hello world"
# 下标从0开始，-1代表最后一个元素，然后负值倒序
# print(str[-1])
# 切片运算
# print(str[0:5])
# print(str[:5])  # 同上
# print(str[-5:])	# 从后向前五个字符
# print(str[-1::-1]) # 逆
# print(str[:])	# 同复制

# 列出对象所封装的方法
# print(dir(str))
# print(help(str.strip))
# 查看方法的解释说明

str=" hello world "
# 去除前后空格
# print(str.strip())
# print(str.lstrip())
# print(str.rstrip())
# 查找字符串
# print(str.find("hello"))	# 找不到返回-1
# print(str.rfind("hello"))	# 反向查找
# print(str.index("hello"))	# 找不到抛异常
# print(str.rindex("hello"))	# 反向查找
# print(len(str))	# 返回字符串长度
# 替换
# print(str.replace(" ","-",1))
# 统计
# print(str.count("-"))
# 分割
# str.split(maxsplit=?)	# 参数代表最大分割数
# str.split(sep=?)	# 指定分隔符为?
# print(str.split())
# 拼接(+即可)
# print(str + "!")
# 列表拼接
s="*"
str="hello world !".split()
# print(s.join(str))

str="hello world"
# 判断以什么开始
# print(str.startswith("h"))
# 判断以什么结束
# print(str.startswith("l"))
# 填充
# print(str.center(20))	# 默认以空格两边填充
# print(str.center(20,"*"))
# print(str.ljust(20,"*"))	# 左对齐，右填充
# print(str.rjust(20,"*"))	# 右对齐，左填充
# 判断是否是数字
# print("1".isdigit())
# 判断是否是字母
# print("1".isalpha())

# 列表
l=[]
print(type(l))
# 列表元素任意类型
l=[1,"s"]
# 尾部添加
l.append(3.5)
# 任意下标添加
l.insert(2,2)
# 拼接序列
l.extend("ab")	# 在原来基础添加
l2=l+"c d".split() # 返回一个新列表
# 遍历
for x in l:
	print(x,end=" ")
print()

import random
# 随机选择
print(random.choice(l))

# 查看内存地址
print(id(l))

# 元组
y=("a","b",1)
for i in range(0,len(y)):
	print(y[i])
# 元组中一个元素时，需要加逗号，区别类型
print(type((1)),type((1,)))

# 字典
m={"a":10,"b":25,"c":{"e":55}}
print(m["c"]["e"])
print(m.get("b"))
# 信息
print(m.items())
print(m.keys())
# 遍历
for k,v in m.items():
	print("%s:%s"%(k,v))
# 清空
m.clear()
