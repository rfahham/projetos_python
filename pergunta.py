#!/usr/local/bin/python
# -*- coding: utf-8 -*-


print '''
Quem descobriu o Brasil?

Selecione a resposta correta:

(a) Rui Barbosa
(b) Marechal Deodoro da Fonseca
(c) Pedro Alvares Cabral
'''

while True:
    resposta = raw_input('R: ')

    if resposta == 'a':
        print 'Você errou'

    elif resposta == 'b':
        print 'você errou' 
                      
    elif resposta == 'c':  
        print 'Você acertou, Parabéns !!!'
        break

