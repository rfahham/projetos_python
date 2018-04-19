#!/usr/bin env python

import time

arq = open('lista.txt', 'a')

nome = raw_input("Informe seu nome: ")
idade = raw_input("Informe sua idade: ")
sexo = raw_input("Informe seu sexo: ")

buffer = 'Nome: '+ str(nome)  + ' Idade:' + str(idade) + ' Sexo: ' + str(sexo)
print(buffer)


arq.write(time.asctime() + ' ' +str(nome) + ' ' + str(idade) + ' ' + str(sexo)+ '\n')
arq.close()