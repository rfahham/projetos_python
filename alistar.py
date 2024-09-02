#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# Código
import time
from datetime import date

atual = date.today()

nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade ==18:
	print('Você tem que se alistar IMEDIATAMENTE !')
elif idade < 18:
	saldo = 18 - idade
	print('Ainda faltam {} anos para o alistamento!'.format(saldo))
elif idade > 18:
	saldo = idade - 18
	print('Você já deveria ter se alistado há {} anos!'.format(saldo))



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