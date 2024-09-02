#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Código
import random

nome1 = str(raw_input('Primeiro aluno: '))
nome2 = str(raw_input('Segundo aluno: '))
nome3 = str(raw_input('Terceiro aluno: '))
nome4 = str(raw_input('Quarto aluno: '))

nomes = [nome1, nome2, nome3, nome4]

serie = ['Peito', 'Costas', 'Biceps', 'Triceps']

escolhido = random.choice(nomes)
exercicio = random.choice(serie)

print('O atleta {} vai executar o exercício de {}'.format(escolhido, exercicio))

# Biblioteca

# print('{}'.format())
# variável = int(input(''))
# variável = float(input(''))
# variável = str(input(''))
