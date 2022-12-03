#!/usr/local/bin/python
# -*- coding: utf-8 -*-


print ('''
========================
Quem descobriu o Brasil?
========================

Selecione a opção correta:

(a) Rui Barbosa
(b) Marechal Deodoro da Fonseca
(c) Pedro Alvares Cabral

''')

while True:
    resposta = input('Opção: ')

    if resposta == 'a':
        print ('Você errou!')
        print ()

    elif resposta == 'b':
        print ('você errou!' )
        print ()
                      
    elif resposta == 'c':  
        print ('Você acertou! Parabéns !!!')
        print ()
        break

