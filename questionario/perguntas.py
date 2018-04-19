#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from random import randint
import linecache
import os
import time

#Limpa a tela
os.system('clear')

#print (randint(0,9))

#Pega o numero de linhas e cria um array
numero_linhas_perguntas = sum(1 for line in open('perguntas.txt'))
#arquivo_linhas = range(num_lines)
#Lista a quantidade de perguntas em nosso banco de perguntas
print ''
print "Atualmente temos" ,numero_linhas_perguntas, "perguntas em nosso banco"
print ''
numero_randomico = (randint(1,numero_linhas_perguntas))
pergunta_selecionada = linecache.getline('perguntas.txt',(numero_randomico))
print '='*50
print pergunta_selecionada

for i in range(3):
    print(".")
    time.sleep(1)

print "Quem vai responder a esta pergunta será:"
time.sleep(2)
numero_linhas_alunos = sum(1 for line in open('alunos.txt'))
numero_randomico_aluno = (randint(1,numero_linhas_alunos))
aluno_selecionado = linecache.getline('alunos.txt',(numero_randomico_aluno))
print ''

for i in range(3):
    print(".")
    time.sleep(1)

print aluno_selecionado