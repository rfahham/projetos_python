#!/usr/bin/env python 
# -*- coding: utf-8 -*-

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
	print('{} - '.format(c))



