#!/usr/bin/env python 
# -*- coding: utf-8 -*-

preco = float(input('Qual é o preço do produto? R$ '))
desconto = float(input('Qual o valor do desconto? '))
novo = preco - (preco * desconto / 100)

print('O produto que custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f}.'.format(preco, desconto, novo))


# 1500*10/100

# 1500 valor
# 10 desconto
# 100 por cento

