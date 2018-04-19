#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Código
import random

# nomes = ['Sillas', 'João Borsani', 'Rodrigo Iagi', 'Ricardo Fahham', 'Bruno Medeiros', 'Roberto Cesar'  ]


nome1 = str(raw_input('Primeiro participante: '))
nome2 = str(raw_input('Segundo participante: '))
nome3 = str(raw_input('Terceiro participante: '))
nome4 = str(raw_input('Quarto participante: '))

nomes = [nome1, nome2, nome3, nome4]

questionario = ['Raiz quadrada de 4? ',
				'Quem descobriu o Brasil? ',
				'Qual é o dia do Indio? ',
				'Lula está ...']


escolhido = random.choice(nomes)
perguntas = random.choice(questionario)

print('')
print('O participante {} vai responder: {}'.format(escolhido, perguntas))
print('')

# Biblioteca

# print('{}'.format())
# variável = int(input(''))
# variável = float(input(''))
# variável = str(input(''))
