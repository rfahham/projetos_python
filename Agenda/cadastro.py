#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import sqlite3

conectar = sqlite3.connect('agenda.db')
c = conectar.cursor()

#SQL - Criar banco de Dados

def criar_db():
	c.execute('CREATE TABLE cadastro (Nome text, Idade int, Sexo text)')

try:
	criar_db()
except:
	print('Banco de Dados ja existe !!!')
else:
	print('Banco de Dados criado com Sucesso !!!')

def inserir(n,i,s):
	c.execute('INSERT INTO cadastro VALUES(?,?,?)', (n,i,s))
	conectar.commit()


fc = int(input('Digite uma opção:\n\n1 - Cadastrar\n2 - Consultar\n\n'))

# Cadastra / Consultar
if fc == 1:
	try:
		print('Cadastro Agenda')
	 	n = str(raw_input("Informe seu nome: ")) # raw_input não funciona no Python 3
		i = int(raw_input("Informe sua idade: "))# raw_input não funciona no Python 3
		s = str(raw_input("Informe seu sexo: "))# raw_input não funciona no Python 3
	  	inserir(n,i,s)
	except: # caso não de cer to 
	    print('Erro ao cadastrar dados !!!')
	else: # Caso de certo 
	    print('Cadastrado efetuado com Sucesso !!!')
elif fc == 2:
	print('agenda.db')

else:
	print('...')

