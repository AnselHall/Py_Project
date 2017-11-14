#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'面向对象编程 高级编程'

__author__ = 'Junguo'


print(__author__)

'''

	创建一个 class 实例，可以给该实例绑定任何属性和方法，不过这里动态绑定的属性和方法只对该实例有效，对该对象的其他实例无效。

	如果想对都有实例都起作用，可以给该对象绑定。


	如果想要限制实例的属性，比如只允许对对象的某些实例进行绑定操作。使用 __slots__
		使用 __slots__ 定义的属性仅对当前类实例起作用，对继承的子类不起作用。


'''

class Student(object):
	__slots__ = ("name","age") # 通 tuple 定义允许绑定的属性名称

s = Student() #实例化对象
s.name = 'Michael' #绑定属性 ‘name’
s.age = 29 #绑定属性 ‘age’
#s.score = 80 # 绑定属性 ‘score’ 报错，该属性没有定义


'''

	使用 @property

'''

class Techer(object):
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an interger')
		if value <0 or value > 100:
			raise ValueError('score must between 0 - 100')
		self._score = value


t = Techer()
t.score(1000)