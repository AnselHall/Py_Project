#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

    每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，
    也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。

'''
import sys

__author__ = 'Junguo'


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello,World %s' % args[0]) # /Users/qiunanjin/Desktop/Junguo/Py_Project/com.ansel/__init__.py
    elif len(args) == 2:
        print('Hello,%s1' % args[1])
    else:
        print('Too Many arguments')


if __name__ == '__main__':
    test()


# from PIP import Image
print(sys.path)
'''
['/Users/qiunanjin/Desktop/Junguo/Py_Project/com.ansel', 
 '/Users/qiunanjin/Desktop/Junguo/Py_Project', 
 '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', 
 '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6', 
 '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', 
 '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']

'''
