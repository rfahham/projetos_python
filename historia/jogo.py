#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect('cadastro.db')
#print "Opened database successfully";
cursor = connection.cursor()

#SQL


# lendo os dados
cursor.execute('SELECT * FROM dados')

sql_id = 'SELECT * FROM dados WHERE id = ?'
sql_pergunta = 'SELECT * FROM dados WHERE pergunta = ?'
sql_resposta = 'SELECT * FROM dados WHERE resposta = ? ? ?'
sql_resposta_certa = 'SELECT * FROM dados WHERE resposta_certa = ?'




# for linha in cursor.fetchall():
#     print(linha)

# pergunta = input('Qual a resposta certa? Escolha A, B ou C')

# while True:
#      resposta = raw_input('R: ')

#      if resposta == 'a':
#         print 'Você errou'

#      elif resposta == 'b':
#         print 'você errou' 
                      
#      elif resposta == 'c':  
#         print 'Você acertou, Parabéns !!!'
#         break

# #resposta 
# print 'Resposta Certa !'

connection.close()



