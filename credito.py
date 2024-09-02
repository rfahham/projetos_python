#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# Código
print('')
print('OBS: Valor da prestação tem que ser menor ou igual a 30% do salário do comprador para ser CONCEDIDO')
print('')
casa = float(input('Digite o valor do crédito: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
minimo = salario * 30 / 100

prestacao = casa / (anos * 12)
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos))
print('A prestação será de R$ {:.2f}'.format(prestacao))

if prestacao <= minimo:
	print('\033[32mEmpréstimo pode ser CONCEDIDO!\033[m')
else:
	print('\033[31mEmpréstimo NEGADO!\033[m')

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