#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Código

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos kms rodados? '))
valor = float(input('Valor do KM rodado? '))
pago = (dias * valor) + (km + 0.15)
print('O total a pagar é de R$ {}'.format(pago))

# Biblioteca

# print('{}'.format())
# variável = int(input(''))
# variável = float(input(''))