def pline():
	print("-"*30)
pline()

# 创建类
class Person(object):
	# 类属性
	age = 25
	code="lrx"
	# 方法重写
	def __init__(self,name):
		print("__init__")
		# 实例属性(公有属性)
		self.name=name
		# 私有属性（加__）
		self.__gender="女"
	# 实例方法，可以访问类属性和对象属性，只能用对象调用
	def eat(self,food):
		print("%s正在吃%s"%(self.name,food))

	# 类方法，可以访问类属性，不能访问对象属性，可以被对象和类名调用
	@classmethod
	def sleep(self,time):
		print("%s在%s点睡觉"%(self.code,time))

	# 静态方法，不可以访问对象和类属性，可以被类名调用
	@staticmethod
	def getAge(name):
		print("%s今年25岁了"%name)

	# 私有
	def __test(self):
		print("私有方法")

a1=Person("ly")
a1.name="lgm"
a1.eat("面包")
print(Person.age)

a1.sleep("七")
Person.sleep("八")

Person.getAge("ly")
# 打印当前对象所有属性和方法
print(dir(a1))
# 打印私有属性
print(a1._Person__gender)

# 继承
class girl(Person):
	def __init__(self,name):
		# Person.__init__(self,name)
		# super(girl,self).__init__(name)
		super().__init__(name)

	def __str__(self):
		return ("%s爱唱歌"%self.name)

g=girl("lsc")
print(g)

class boy(object):
	pass
# 多继承
class supem(Person,boy):
	pass

import random
# 随机数
print(random.randint(1,7))
































