#!/usr/bin/env python 
# -*- coding: utf-8 -*-

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opcao = 0
while opcao != 5:
    print('''	
    	[ 1 ] Somar
    	[ 2 ] Multiplicar
    	[ 3 ] Maior
    	[ 4 ] Novos Números
    	[ 5 ] Sair do Programa
    	''') 

    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
    	soma = n1 + n2
    	print('A soma entre {} + {} é {}' .format(n1, n2, soma))

    elif opcao == 2:
    	produto = n1 * n2
    	print('O resultado de {} x {} é {}' .format(n1, n2, produto))

    elif opcao == 3:
    	if n1 > n2:
            print('O número {} e o maior'.format(n1))
        if n2 > n1:
            print('O número {} e maior'.format(n2))
        if n1 == n2:
        	print('O número {} é igual ao número {}'.format(n1, n2))

    elif opcao == 4:
    	print('Informe os números novamente: ')
	n1 = int(input('Primeiro Valor: '))
	n2 = int(input('Segundo Valor: '))
    elif opcao == 5:
    	print('Finalizando...')

    else:
    	print('Opção inválida. Digite uma opçõa válida!')
    
print('Fim do programa! Volte Sempre!')
