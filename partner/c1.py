# 实例001：数字组合
# 题目 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
#
# 程序分析 遍历全部可能，把有重复的剃掉。
# 方法一：
# total = 0
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if ((i != j) and (j != k) and (k != i)):
#                 print(i, j, k)
#                 total += 1
# print(total)

# 方法一拓展：
# 拓展：
a = ([2, 5, 6, 7])
print('有四个数字：', a, '能组成互不相同且无重复数字的三位数如下：')
total = 0
for i in a:
    for j in a:
        for y in a:
            if (i != j) and (j != y) and (y != i):
                print(i, j, y)
                total += 1
print('*************************')
print('组成的数字一共为', [total], '个')


# # 方法二，简便方法 用itertools（itertools --- 为高效循环而创建迭代器的函数）中的permutations（permutations() p[, r]
# 长度r元组，所有可能的排列，无重复元素）即可。
#
# import itertools
#
# sum2 = 0
# a = [1, 2, 3, 4]
# for i in itertools.permutations(a, 3):
#     print(i)
#     sum2 += 1
# print(sum2)

