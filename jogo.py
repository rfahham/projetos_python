#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from random import randint

n = int(randint(1, 9))
p = 0
t = 0
while p != n:
	p = int(input("Seu palpite: "))
	t += 1
	if p == n:
		print ("Acertou! Placar %i" % t)
	elif p < n:
		print("Entre com um número maior")
	else:
		print("Entre com um número menor")
print("Fim do Jogo")

