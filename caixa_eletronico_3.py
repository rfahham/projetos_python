#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# Código

print('='*35)
print('BANCO CEV'.center(35))
print('='*35)

n = int(input('Que valor você quer sacar? R$ '))
n50 = n // 50
n20 = (n % 50) // 20
n10 = ((n % 50) % 20) // 10
n1 = ((n % 50) % 20) % 10
if n50 > 0:
    print('Total de {} cédulas de R$50'.format(n50))
if n20 > 0:
    print('Total de {} cédulas de R$20'.format(n20))
if n10 > 0:
    print('Total de {} cédulas de R$10'.format(n10))
if n1 > 0:
    print('Total de {} cédulas de R$1'.format(n1))


print('='*35)
print('Volte sempre ao BANCO CEV!')
# print('Tenha um bom dia!')﻿




# Biblioteca

# print()
# print('')
# print('{}'.format())
# print('{:.2f}'.format())
# 


# variável = int(input(''))
# variável = float(input(''))
# variável = str(input(''))

# cores código ANSI

# STYLE			TEXT				BACK
# 0 none		30 Branco			40 Branco
# 1 bold		31 Vermelho			41 Vermelho
# 4 Underline	32 Verde			42 Verde
# 7 Negative	33 Amarelo			43 Amarelo
#				34 Azul				44 Azul	
#				35 Roxo				45 Roxo
#				36 Azul Claro		46 Azul Claro	
#				37 Cinza			47 Cinza
#
# EXEMPLO			
# print('\033[31mMULTADO!\033[m ')
#
# cores = {
#			'limpa':'\033[m',	
#			'azul':'\033[34m',	
#			'amarelo':'\033[33m',	
#			'pretoebranco':'\033[7;30m',	
#         }
#
# print('Meu nome é {}'.format(cores['pretoebranco'], nome, cores['limpa']))