#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# Cateto oposto
# co = float(input('Comprimento do cateto oposto: '))
# Cateto adijacente
# ca = float(input('Comprimento do cateto adijacente: '))
# hi = (co ** 2 + ca ** 2) ** (0.5)

# print('A hipotenusa vai medir {:.2f}'.format(hi))

# h1 = co ** 2

# print h1

# h2 = ca ** 2

# print h2

# h3 = co ** 2 + ca ** 2

# print h3

# h4 = h3 ** 0.5

# print ('{:.2f}'.format(h4))

from math import hypot

# Cateto oposto
co = float(input('Comprimento do cateto oposto: '))
# Cateto adijacente
ca = float(input('Comprimento do cateto adijacente: '))

hi = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))
