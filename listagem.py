#!/usr/bin/env python 
# -*- coding: utf-8 -*-

#Imprime listagem de 1 a 50 
for n in range(1, 51):
	print('{} - '.format(n))

print('-' * 12)

# Imprime somente números pares
for n in range(1, 51):
	if n % 2 == 0:
		print('{} - '.format(n))

print('-' * 12)

# Diminui os laços para geral o resultado
for n in range(2, 51, 2):
	print('{} - '.format(n))
	