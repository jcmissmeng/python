#主要遍历。循环序列或者集合字典
# 

# a = [1,2,3]

# for x in a:
#     if x == 2:
#        continue   #break 打破循环后，直接输出，不执行后面语句！
#     print(x)
# else:
#     print('EOF')


""" a = [['apple','orange','banana','grape'],(1,2,3)]
for x in a:
    # if 'banana' in x:
    #     break
    for y in x:
        if y == 'orange':
            break
        print(y)
else:
    print('fruit is gone') """

""" #打印出0-9数字：range 产生序列。python中没有i++语句。
for x in range (10,0,-2):    #2为步长。打印结果为：02468   括号中：小的数如：0在前，步长为2.则按照正序排列。10在前，步长需为-2，按照倒序排列。
    print(x,end= ' | ')  #输出为：递增等差数列 """


""" #习题：打印出a = [1,2,3,4,5,6,7,8]中的间隔数字。
a  = [1,2,3,4,5,6,7,8]
for i in range(0,len(a),2):
    print(a[i],end=' | ') """
#利用切片间隔取数
# a = [1,2,3,4,5,6,7,8]
# b = a[0:len(a):2]
# print (b)

# 高性能，封装性（可重复）,抽象
# """ 包：

# """ python中包的标志标志为：需要有一个文件名为：_init_.py """
# 包的导入，要注意顺序！使用：语句：import X.py
# 如果要使用包中的某个变量：print(X.a)使用X包中的变量a """

#简化：当要导入的包名称太长，不便使用，需要使用语句：import t.c7 as m  讲t包中的c7作为m
# 导入包的另一方法：
from t import c7
print (c7.a)