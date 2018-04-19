#!/usr/bin/env python 
# -*- coding: utf-8 -*-

print('Sequência de Fibonacci')
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(t1)
print(t2)
cont = 3
while cont <= n:
	t3 = t1 + t2
	print('{}' .format(t3))
	t1 = t2
	t2 = t3
	cont += 1
print('FIM')
