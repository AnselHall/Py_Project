#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print('hello python')
"""
    多行注释
"""

'''
    条件判断
'''
height = 1.8
weight = 75

bmi = weight / (height * height)

print('bmi = ', bmi)

if bmi > 32:
    print('严重肥胖')
elif bmi > 28:
    print('肥胖')
elif bmi > 25:
    print('过重')
elif bmi > 18.5:
    print('正常')
else:
    print('正常')

print('###############  分割线   ################')

'''
    循环
'''
# for 循环
names = ['Michael', 'Bob', 'Tracy']

for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x

print(sum)

print('计算 1 - 100 的和')
sum = 0
for x in range(101):  # rang 函数，会生成101个整数序列 0 - 100
    sum = sum + x

print(sum)

# while 循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

print('请利用循环依次对list中的每个名字打印出Hello, xxx!')
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello,', name)

print('break : 在循环中，break语句可以提前退出循环。')
n = 0
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('End')

print('在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。')
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

print('要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。'
      '大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。')

print('########################################################################')

'''
    dict：字典，其他语言中也称为 map，使用 key - value 存储，具有快速的查找速度
    特点：请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
        1、查找和插入的速度极快，不会随着 key 的增加而变慢
        2、需要占用大量的内存，内存浪费多
    list 相反：
        1、查找和插入的时间随着元素的增加而增加
        2、占用空间小，浪费内存很少
    所以 dict 是用空间换时间的一种方法
    
    dict ：
        1、dict 的 key 必须是不可变对象
    
    
    set：和 dict 类似，也是一组 key 的集合，但不存储 value。由于 key 不能重复，所以，在 set 中，灭有重复的 key。

'''
d = {'Michael': 90, 'Bob': 89, 'Tracy': 20}
print(d['Michael'])

s = {1, 2, 3}  # 等价于  s = set([1,2,3])
print(s)
