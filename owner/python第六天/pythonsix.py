# 实现多态
class Animal(object):
	def run(self):
		pass

class Dog(Animal):
	def run(self):
		print("小狗在街上跑。。。")

class Bird(Animal):
	def run(self):
		print("小鸟在天上飞。。。")

class Fish(Animal):
	def run(self):
		print("小鱼在水里游。。。")

def start(ll):
	for animal in ll:
		# 判断类型是否相同
		if isinstance(animal,Animal):
			animal.run()

l=[Dog(),Bird(),Fish()]
start(l)

# sublime text3 快捷键 ctrl+shift+k：删除整行 Ctrl+K+U/Ctrl+K+L 转换大小写 ctrl+l 选中整行

# __new__()
class Person(object):
	def __init__(self,name):
		print("__init__%s"%name)
		self.name=name
		
	def __new__(cls,name):
		print("__new__%s"%name)
		return object.__new__(cls)

	def __str__(self):
		return "hi,%s"%self.name

p=Person("lgm")
print(p)

# 单例模式
# 第一种通过结合类属性创建
class SingleA(object):
	def __init__(self,name):
		self.name=name

	instance=None

	@classmethod
	def getInstance(cls,name):
		if cls.instance==None:
			cls.instance=SingleA(name)
		return cls.instance

p1=SingleA.getInstance("lgm")
p2=SingleA.getInstance("lrx")

# 存在问题
p3=SingleA("lgm")
p4=SingleA("lrx")

print(p1,p2,p3,p4)

# 第二种通过结合__new__方法
class SingleB(object):
	instance=None

	def __init__(self,name):
		self.name=name

	def __new__(cls,name):
		if not cls.instance:
			cls.instance=object.__new__(cls)
		return cls.instance

p5=SingleB("lgm")
p6=SingleB("lrx")

print(id(p5),id(p6))

# 简单工厂模式
class Worker(object):
	def __init__(self,name):
		self.name=name

	def work(self,tool):
		print("%s要开始工作了"%self.name)
		wtool=ToolFactory.getTool(tool)
		wtool.cutTree()

	# 抽象工厂
	def absWork(self,fac):
		print("%s要开始工作了"%self.name)
		wtool=fac.project()
		wtool.cutTree()

# 产品类
# 基类
class ETool(object):
	def __init__(self,name):
		self.name=name

	def cutTree(self):
		print("用%s进行工作"%self.name)

# 子类
class StoneExe(ETool):
	def __init__(self,name="石斧"):
		self.name=name
class SteelExe(ETool):
	def __init__(self,name="铁斧"):
		self.name=name

# 工厂类
class ToolFactory(object):
	@staticmethod
	def getTool(tool):
		if tool=="stone":
			return StoneExe()
		elif tool=="steel":
			return SteelExe()
# 验证简单工厂模式
p=Worker("JC")
p.work("stone")

# 抽象工厂
# 工厂基类
class EFactory(object):
	def __init__(self):
		pass
	def project(self):
		pass

# 工厂子类
class StoneFactory(EFactory):
	def project(self):
		return StoneExe()

class SteelFactory(EFactory):
	def project(self):
		return SteelExe()

# 验证抽象工厂模式
q=Worker("JC")
q.absWork(SteelFactory())



