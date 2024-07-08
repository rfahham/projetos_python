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
    "Luiz": 3000,
}

meta = 3000

bateu_meta = [vendedor for vendedor in vendedores if vendedores[vendedor]>=meta]

print(bateu_meta)