#!/usr/bin/python
# -*- coding: utf-8 -*-

# print 'Quem descobru o Brasil ?'
# answer = raw_input("Digite a resposta: ")
# var1 = "Pedro Alvares Cabral"

# print(var1)
# print(answer)

# if (answer == var1):
#    print "Correto !"
# else:
#    print "Errou !"
#    print var1

# print "Good bye!"



print 'Quem descobru o Brasil ?'
print 'Selecione a resposta correta:'
print '1 - Pedro Alvares Cabral'
print '2 - Fulano'
print '3 - Ciclano'

var1 = '1'
var2 = '2'
var3 = '3'

answer = raw_input("Selecione a opção correta: ")

if (answer == var1):
   print "Correto !"
else:
   print "Errou !"

print "Good bye!"