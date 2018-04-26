#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# Código

print('=' * 50)
# print('{:^30}'.format('ZIP MALDITO') * 60)
print('{:^50}'.format('Bem vindo ao Banco CEV'))
print('=' * 50)

valor = int(input('Que valor você quer sacar? R$ '))

total = valor 

cedula = 100

totalcedula = 0
while True: 
	if total >= cedula:
		total -= cedula
		totalcedula += 1
	else:
		if totalcedula > 0:
			print('Total de {} cédulas de R${}'.format(totalcedula, cedula))
		if cedula == 100:
			cedula = 50
		elif cedula == 50:
			cedula = 20
		elif cedula == 20:
			cedula = 10
		elif cedula == 10:
			cedula = 5
		elif cedula == 5:
			cedula = 1
		totalcedula = 0	
		if total == 0:
			break

print('=' * 50)
# print('{:^30}'.format('ZIP MALDITO') * 60)
print('{:^50}'.format('Vonte sempre ao Banco CEV'))
print('=' * 50)



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