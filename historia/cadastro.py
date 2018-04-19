#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect('cadastro.db')
c = connection.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS dados (id integer, pergunta text, resposta1 text, resposta2 text, resposta3 text, resposta_certa text)')
create_table()

def dataentry():
	c.execute("INSERT INTO dados VALUES(1, 'Quem descobriu o Brasil?', 'Rui Barbosa', 'Marechal Deodoro da Fonseca', 'Pedro Alvares Cabral', 'Pedro Alvares Cabral' )")
	c.execute("INSERT INTO dados VALUES(2, 'Ano que a familia Imperial chegou ao Brasil?', 1808, 1822, 1889, 1808)")
	connection.commit()
	print 'Tabela criada com sucesso.'

dataentry()