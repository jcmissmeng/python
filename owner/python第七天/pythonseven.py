# 被导入其他模块中显示模块名
print(__name__)

import sys
# 基础模块
# print(sys.modules)

def fun():
	"函数使用说明"
	print("使用说明")

class Person:
	"类使用说明"
	pass

if __name__ == "__main__":
	fun()
	print(sys.path)


# 模块发布
# from distutils.core import setup
# print(setup.__doc__)

# 在setup.py中设置基本信息
# 名称，版本，描述，作者，文件信息
# setup(name="",version="",description="",author="",py_modules=[])
# 下一步命令行（当前路径下），输入：
# 	 python setup.py build # 编译
# 	 python setup.py sdist # 生成压缩包

# 模块安装
# 先解压安装包
# 在此路径下，打开命令行输入：
# 	python setup.py install

# 列表推导式 针对有规律的列表
l=[i for i in range(1,10) if i%2==0]
print(l)

l=[(x,y) for x in range(1,3) for y in range(2,4)]
print(l)
a,*b=l
print(a,b)

strings = ['import','is','with','if','file','exception']  
D = {key: val for val,key in enumerate(strings)}  
print(D)






