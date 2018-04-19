#!/usr/bin/env python3
# -*- coding: utf-8 -*-

connection = sqlite3.connect('pergunta_resposta.db')
c = connection.cursor()

#SQL

sql = 'SELECT * FROM dados WHERE id = ?'

def read_data(wordUsed):
	for row in c.execute(sql, (wordUsed,)):
		print row

read_data('id')







# print (pergunta.a)

# while True:
#      resposta = raw_input('R: ')

#      if resposta == 'a':
#         print 'Você errou'

#      elif resposta == 'b':
#         print 'você errou' 
                      
#      elif resposta == 'c':  
#         print 'Você acertou, Parabéns !!!'
#         break



