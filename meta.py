#!/usr/bin/env python 
# -*- coding: utf-8 -*-

print("-"*70)
print("Verifica o somatório de vendas e compara com a meta estipulada")
print("-"*70)
print("")

vendedores = {
    "João": 1500,
    "Marlon": 5000,
    "Ana": 3500,
    "Andre": 5500,
    "Maria": 4000,
    "Luiz": 2500,
    }

print("Nome dos vendedores:")
print(vendedores.keys())
print("")

print("Valor total das vendas:")
print(vendedores.values())
print("")

print("Imprimindo o dicionário:")
print(vendedores.items())
print("")

# Valor da meta
meta = 3000

# Função que verifica quais vendedores batetam a meta
bateu_meta = [vendedor for vendedor in vendedores if vendedores[vendedor]>=meta]
print("Vendedores batetam a meta:")
print(bateu_meta)
print("")

# Função que verifica quais vendedores batetam a meta
nao_bateu_meta = [vendedor for vendedor in vendedores if vendedores[vendedor]<=meta]
print("Vendedores que não batetam a meta:")
print(nao_bateu_meta)
print("")