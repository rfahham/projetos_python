#!/usr/bin/env python 
# -*- coding: utf-8 -*-

print('=' * 30) 
print('Sequência de Fibonacci'.center(30))
print('=' * 30)

def function():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for i in function():
    if i > 100:
        break
    print(i, end = ' ')

    