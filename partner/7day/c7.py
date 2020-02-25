# 20200219日课程笔记——python的高级语法

# 类型 枚举的特点以及使用。

from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4



# 别名

class Commom():
    YELLOW = 1
""" print(type(VIP.RED.name))  
print(type(VIP.RED)) 
print(type(VIP.RED.value)) """
# 后面的类型不一样，依次如下：
# 枚举的类型、枚举的名字、枚举的值
# .name对应的是  <class 'str'>
# <enum 'VIP'>
# .value对应的的是 <class 'int'>

""" #  枚举可遍历

for v in VIP:
    print(v) """

# 枚举的比较  不支持大小比较 

# 不可以 result = VIP.GREEN > VIP.BLACK
result = VIP.GREEN is VIP.BLACK
print(result)