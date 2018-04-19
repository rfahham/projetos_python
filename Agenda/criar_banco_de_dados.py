#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# https://www.youtube.com/watch?v=1RjEnbLymN4

# Criação do Banco de Dados

import sqlite3, time

conectar = sqlite3.connect('dados.db')
c = conectar.cursor()

def criar_db():
	c.execute('CREATE TABLE IF NOT EXISTS cadastro (id integer, nome text, idade integer, email text)')

try:
	criar_db()
except:
	print('Banco de dados já criado!!!')
else:
	print('Banco de dados criado com sucesso!!!')

	



