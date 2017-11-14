#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

    函数式编程
'''

# 高阶函数 High-order function
from functools import reduce

print(abs(-100))


def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))

## 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。

'''
    Python 內建函数 map() reduce()
    
    map()
        接收两个参数，一个是函数，一个是 Iterable，map 将传入的函数依次作用到序列的每个元素，并把结果作为新的 Iterable 返回。
        
    reduce()
        把一个函数作用在一个序列 [x1,x2,x3,....] 上，这个函数必须接收两个参数，reduce 把结果继续和序列的下一个元素做累积计算，
        
    filter()
        接收一个函数和一个序列，将传入的函数作用于每个元素，根据返回值决定保留还是丢弃
        
    sorted()
        排序算法：可以排序数字
            也可以指定排序方式，key = ,将 key 指定的函数应用到每个元素上，并根据 key 函数返回的结果进行排序。
            排序字符串是根据字母的 ASCII 码的大小
            可以正序排列或反序排序 reverse = True
        
'''


def f(x):
    return x * x


r = map(f, [1, 3, 4, 5, 4])
print(list(r))  # map 返回的是 Iterable 对象，需要转换为 list 才能打印


def f(x, y):
    return x + y


s = reduce(f, [1, 3, 4, 6, ])
print(s)

L = ['adam', 'LISA', 'barT']


def normalize(name):
    if isinstance(name, str):
        n = name.lower()
        return n
    else:
        return ''


L1 = list(map(normalize, L))
print(L1)


def f(x, y):
    return x * y


L = [3, 5, 7, 9]


def prod(L):
    return reduce(f, L)


print('3 * 5 * 7 * 7 = ', prod(L))


def str2float(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': -10}[s]


a = map(str2float, '124.3535')

print(list(a))


# print('str2float(\'123.456\') =', str2float('123.456'))


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        if n > 1000:
            break
        yield n


def _not_divisible(n):
    return lambda x: x & n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


print(list(primes()))


def is_palindrome(n):
    s = list(str(n))  # 数字 转字符串 转序列
    mid = len(s) // 2  # //代表地板除
    p1 = s[:mid + 1]
    p2 = s[mid:]
    p2.reverse()  # reverse()函数将序列反转
    if p1 == p2:
        return True
    else:
        return False


output = filter(is_palindrome, range(1, 1000))
print(list(output))

print('\n\n\n\n\n\n\n')

print(sorted([1, 4, 5, 200, 9, -10, -100, 30]))
a = sorted([36, 5, -12, 9, -21], key=abs)
print(a)

print(sorted(['bob', 'about', 'Zoo', 'Credit']))
s = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(s)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


def by_score(t):
    return t[1]


print(sorted(L, key=by_name))

print(sorted(L, key=by_score))

print('\n\n\n\n\n')

'''
    返回函数：高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
    
        注意：返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能变化的变量。
        
    闭包：闭包就能能够读取其他函数内部变量的函数
'''

'''
    匿名函数
    
'''

'''
    装饰器：在代码运行期间动态增加功能的方式。Decorator
    
'''
#
# def now():
#     print('2017-11-13')
#

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2017-11-13')

now()

now = log(now)

now()

'''
    偏函数：Partial function：把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个函数会更简单。
'''