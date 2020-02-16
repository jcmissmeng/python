""" # 代码块
# if condition:
#     if condition:
#         pass
#     else:
#         pass
# else:
#     if condition:
#         pass
#     else:
#         pass

# 练习要实现的功能，输入a = x，打印出所代表的字符串。

# a = 1 print('apple')
# a = 2 print('orange')
# a = 3 print('banana')

# print('shoping') """

a = input()
# 错误总结：运行后输入1不显示代表字符串，无报错，但总是出现shopping。
# 原因如下： 数据类型，input 是字符串，if中是int型，需要将输入的类型，转为int型！一定要注意类型！！
# a = int (a)
if a == 1:
    print('apple')
else:
    if a == 2:
        print('orange')
    else:
        if a == 3:
            print('banana')
        else:
            print('shopping')
 
# 如何简化？
# 1、利用 elif
# 2、利用 or 