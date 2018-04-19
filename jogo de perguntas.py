#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randrange

questions = {
	'a': 'Que dia da semana e hoje?',
	'b': 'Como esta o clima?'
}

answer1 = [
	'Domingo',
	'Segunda-feira',  
	'Terça-feira', 
	'Quarta-feira', 
	'Quinta-feira', 
	'Sexta-feira', 
	'Sábado'
	]

answer2 = [
	'Ensolarado e quente',
	'Chuvoso e umido',
	'Frio e seco'
	]

def main():
	while True:
		qst = input('Entre com a pergunta: ')
		if qst == questions['a']:
			print('\n\tHoje e %s\n' %answer1[randrange(len(answer1))])
		elif qst == questions['b']:
			print('\n\tHoje esta %s\n' %answer2[randrange(len(answer2))])
		else:
			print('\n\tDesculpe, nao entendi...\n')

if __name__ == '__main__':
	main() 