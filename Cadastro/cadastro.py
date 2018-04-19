#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# https://www.youtube.com/watch?v=1RjEnbLymN4

# Criação do Banco de Dados

import sqlite3, time

conectar = sqlite3.connect('cadastro.db')
c = conectar.cursor()

def criar_db():
	c.execute('CREATE TABLE IF NOT EXISTScadastro (id integer, unix real, keyword text, datestamp text, value real)')

try:
	criar_db()
except:
	print('Banco de dados já criado!!!')
else:
	print('Banco de dados criado com sucesso!!!')

def dataentry():
	c.execute('INSERT INTO dados VALUES')

	
connection.commit () # gravar dos dados no BD




