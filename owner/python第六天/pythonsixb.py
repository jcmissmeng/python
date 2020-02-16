try:
	print(num)
except (NameError,IOError) as ex:
	print("变量未定义",ex)

# IOError
f=None
try:
	f=open("1.txt")
except Exception as e:
	print("b")
else:
	print("else")
	num=1/0
finally:
	try:
		if not f:
			f.close()
	except Exception as e:
		print("a")

# 自定义异常
class ShortError(Exception):
	def __init__(self,length,atleast):
		super().__init__(self)
		self.length=length
		self.atleast=atleast

	def __str__(self):
		return "ShortError:输入长度%s小于最小的长度%s"%(self.length,self.atleast)

try:
	str="ab"
	if len(str) < 3:
		# 抛出异常
		raise ShortError(len(str),3)
except ShortError as e:
	print(e)
# except OrthreError as e:
	






