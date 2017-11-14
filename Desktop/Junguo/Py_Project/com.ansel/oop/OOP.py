#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'面向对象编程'

__author__ = 'Junguo'

'''
    class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，
    通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
    
    类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

    方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
    
    通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
    
    和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：


'''


class Student(object):
    def __init__(self, name, score):
        self.score = score

        self.name = name

    def print_score(self):
        print('%s : %s' % (self.name, self.score))


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 90)

bart.print_score()
lisa.print_score()

'''
    访问限制：
    
        如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线 __  
        
        需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
        特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。  
        
        
    继承和多态
'''


class Animal(object):
    def run(self):
        print("Animal is running")


class Dog(Animal):
    def run(self):
        print('Dog is running')


class Cat(Animal):
    def run(self):
        print('Cat is running')


d = Dog()

a = type(Dog())  # type() 获取对象的类型

s = dir(Dog())  # 获取对象的所有的属性和方法，返回一个包含字符串的 list，

def test():
    if hasattr(d, 'x'): # 判断 对象有没有指定的属性。这里是判断 Dog 类是否有 'x' 属性
        print('has attr')
    else:
        setattr(d,'x','xxxxx') # 给对象动态设置属性，

        print(d.x)

        print('not have attr')
test()