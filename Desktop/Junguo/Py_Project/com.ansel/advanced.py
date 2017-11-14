#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    高级特性：切片、迭代、列表生成式、生成器、迭代器
'''
from collections import Iterable

import os

print("\n\nPython 高级特许：切片、迭代、列表生成式、生成器、迭代器")
print('\n切片：\n')

L = list(range(100))
print(L)

print(L[:10])  # 取出前10个数
print(L[-10:])  # 取出后十个数
print(L[2:5])  # 取出索引为2到索引为5之间的数，不包括索引为5的数

print(L[:10:2])  # 取出前十个元素，每2个取一个

print(L[::5])  # 没5个取一个

print(L[:])  # 相当于又复制一个 list

# tuple 也是一种 list，也可以用切片处理，处理的结果仍是 tuple
print((1, 3, 4, 5, 6)[:3])

# 字符串也可以看做一种 list，每个元素就是一个字符，所以也可以使用切片，结构仍是字符串
print("Hello world"[1:8:2])

'''
    在很多编程语言中，针对字符串提供了很多各种截取函数（例如，substring），
    其实目的就是对字符串切片。Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。
'''

print('\n\n\n迭代：Iteration\n')
d = {'b': 1, 'a': 2, 'c': 3}
for a in d:  # 遍历 key
    print(a)

for b in d.values():  # 遍历 values
    print(b)

for a, b in d.items():  # 遍历 key：values
    print(a, b)

for a in 'ABC':  # 字符串也可以遍历
    print(a)

# 判断对象是否是可迭代对象
print(isinstance('abc', Iterable))
print(isinstance(1343, Iterable))  # 整数不可迭代

# 如果要对 list 实现类似 Java 那样的下标循环可以使用 Python 内置的 enumerate 函数把 list 变成索引-元素对
for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)

print('\n\n\n列表生成式 List Comprehensions ：是Python内置的非常简单却强大的可以用来创建list的生成式\n')
L = list(range(1, 11))  # 1-20 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(L)

L = [x * x for x in range(1, 11)]  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(L)

L = [x * x for x in range(1, 11) if x % 2 == 0]  # [4, 16, 36, 64, 100]
print(L)

L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)  # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

L = [d for d in os.listdir('.')]  # 列出当前目录下的文件和目录名
print(L)

# for ... in  前面的操作标识对生成的 list 的每一个元素的操作

L = ['Hello', 'World', 18, 'Apple', None]
L1 = [s.lower() for s in L if isinstance(s, str)]  # 在包含各种类型数据的 list 中，将 list 中的字符串中的字符都变为小写。
print(L1)

print('\n\n\n生成器：generator 一边循环一边计算的机制\n')
L = (x * x for x in range(1, 10))  # 这里使用 （）创建 generator，使用 [] 生成的是 list
for a in L:
    print(a)


# 打印斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'Done'


print(fib(10))


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'Done'


print(fib(100))  # <generator object fib at 0x101e6b048>  这时，fib（）就是一个 generator 了


def triangle():

    pass
