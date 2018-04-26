#!/usr/bin/env python
# -*- coding: utf-8 -*-
arq = open('lista.txt', 'w') 
texto = """ 
Lista de Alunos 
---------------- 
João da Silva 
José Lima 
Maria das Dores
ALexandre
Jorge
""" 

print(texto)
arq.write(texto)
arq.close()
