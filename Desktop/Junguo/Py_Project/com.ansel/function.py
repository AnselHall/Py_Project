#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    函数:
        1、使用 def 来定义函数
        2、pass 占位符表示函数是一个空实现或暂时没想好如何实现用占位符
        3、定义函数时，需要确定函数名和参数个数；
        4、如果有必要，可以先对参数的数据类型做检查；
        5、函数体内部可以用return随时返回函数结果；
        6、函数执行完毕也没有return语句时，自动return None。
        7、函数可以同时返回多个值，但其实就是一个tuple。

    函数的参数：
        必选参数（位置参数）、可变参数、关键字参数

'''

# 调用函数：格式转换
import math

print(str(1.23))
print(str(hex(255)))
print(str(hex(1000)))


# 定义函数
def my_function():
    pass  # 这里 pass 相当于一个占位符，表示还没想好做什么或这个函数就是一个空实现（如果没有 pass 就会报错）


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x


print(my_abs(-20))


# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


x, y = move(100, 200, 50, math.pi / 6)

print(x, y)  # 143.30127018922195 225.0

print(move(20, 20, 70, math.pi / 6))  # (80.62177826491072, 54.99999999999999)


def quadratic(a, b, c):
    if a == 0:
        raise TypeError("a can't be zero")
    elif (b * b - 4 * a * c) < 0:
        raise TypeError("无解")
    else:
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
        return x1, x2


print(quadratic(2, 3, 1))  # => (-0.5, -1.0)
print(quadratic(1, 3, -4))  # => (1.0, -4.0)


def power(x):
    return x * x


print(power(5))


def power1(x, n):  # 定义的同名函数后定义的会覆盖前面定义的。
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power1(5, 5))  # 定义的同名函数后定义的会覆盖前面定义的。，这时如果传入 power(5) 就会报错，所以为了兼容以前的代码，需要使用默认参数


def power2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power2(5))
print(power2(5, 3))

'''
    默认参数注意事项:
        1、必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

        2、如何设置默认参数。
        
        3、默认参数必须指向不变对象！
'''


# 可变参数：可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


calc(1, 2, 4, 5, )


# 关键字参数：关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Mechael', 30)  # name: Mechael age: 30 other: {}

person('Bob', 35, city='Beijing')  # name: Bob age: 35 other: {'city': 'Beijing'}

person('Adam', 20, gender='M', job='Engineer')  # name: Adam age: 20 other: {'gender': 'M', 'job': 'Engineer'}


# 命名关键字参数:对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。
def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 20, city='Beijing', job='Engineer')  # Jack 20 Beijing Engineer
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。


# 参数组合：在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

'''
总结：
    Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
    
    默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
    
    要注意定义可变参数和关键字参数的语法：
    
    *args是可变参数，args接收的是一个tuple；
    
    **kw是关键字参数，kw接收的是一个dict。
    
    以及调用函数时如何传入可变参数和关键字参数的语法：
    
    可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
    
    关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
    
    使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
    
    命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
    
    定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。

'''


# 递归函数
def move(n, a, b, c):  # 它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法

    pass
