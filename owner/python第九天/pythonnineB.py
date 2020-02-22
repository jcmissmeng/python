import types

# 创建一个类
class Person(object):
	friend="friend"
	def __init__(self,name=None):
		self.name=name

# 实例化一个对象
p=Person("lgm")
pb=Person("lrx")
print(p.name)

# 为当前对象新增一个属性,但是这样新增一个属性不会适用于新创建的对象
p.sex="girl"
print(p.sex)
# print(pb.sex)		# 会报错

# 动态语言特性，直接修改类的属性
# 类属性的修改只能通过类名，以对象修改只是修改一个实例属性 
Person.sex="girl"
print(p.sex,pb.sex)

# 动态添加类的方法
# 定义个方法
def sleep(self,whe):
	print("%s is sleeping in %s"%(self.name,whe))
# 错误用法
# p.sleep = sleep

# 给实例对象添加方法
p.sleep=types.MethodType(sleep,p)
p.sleep("bed")
# pb.sleep("bed")  # 错误

# 给类动态添加方法
Person.sleep=sleep
pb.sleep("bed")

# 为类添加静态方法和类方法，直接用类名传递即可
@classmethod
def testClass(cls):
	print("this is %s"%cls.friend)

@staticmethod
def testStatic(name="lgm"):
	print("%s is taller"%name)

# 为类添加静态方法和类方法
Person.testClass=testClass
Person.testStatic=testStatic
p.testClass()
pb.testStatic()

# 定义类
class Tercher(object):
	# 限制动态添加属性
	__slots__=("name","age")
	def __init__(self,name):
		self.name=name
class Student(Tercher):
	pass

ta=Tercher("lrx")
ta.age=24
print(ta.age)
# ta.sex="girl" 	# 报错，不允许添加属性

# 子类不受限制
sa=Student("ly")
sa.clazz="1"

# 方法添加不受限制
Tercher.sleep=sleep
ta.sleep("bed")















