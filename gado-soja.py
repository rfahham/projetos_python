#!/usr/bin/env python 
# -*- coding: utf-8 -*-

terra = 1000

# soja -> R$162/saca - 60k
# soja -> produtividade = 3000k/ha

# Gado  -> produtividade = 26 arrobas/ha
# 1 arroba = 15k
# preço do arroba = R$ 240,00

prod_soja = 3000
preco_soja = 162 / 60
faturamento_soja = terra * prod_soja * preco_soja

prod_gado = 26
preco_gado = 275
faturamento_gado = terra * prod_gado * preco_gado

# print(f'{faturamento_soja:,}')
# print(f'{faturamento_gado:,}')

if faturamento_soja > faturamento_gado:
    print("Investir em soja")
else:
    print("Investir em gado")