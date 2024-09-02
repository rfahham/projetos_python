#!/usr/bin/env python 
# -*- coding: utf-8 -*-

print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Valor da Compra: R$ '))
opcao = 0
while opcao != 5:
	print('''	
    		[ 1 ] À VISTA Dinheiro/Cheque 10 porcento de desconto.
    		[ 2 ] À Vista Cartão 5 porcento de desconto.
    		[ 3 ] 2 X no Cartão
    		[ 4 ] 3 X ou mais no Cartão
    		[ 5 ] Sair do Programa
    		''')
	opcao = int(input('Qual é a opção? '))
	if opcao == 1:
		total = preco - (preco * 10/100)
		print('Sua compra terá um desconto de 10% e ficará em R$ {:.2f}.'.format(total))
	elif opcao ==2:
		total = preco - (preco * 5/100)
		print('Sua compra terá um desconto de 5% e ficará em R$ {:.2f}.'.format(total))
	elif opcao ==3:
		total = preco
		parcela = total /2
		print('Sua compra será parcelada em 2X de R${:.2f} SEM JUROS.'.format(parcela))
	elif opcao ==4:
		total = preco + (preco * 20/100)
		totalparcelas = int(input('Quantas parcelas? '))
		parcela = total / totalparcelas
		totalfinal = parcela * totalparcelas
		print('Sua compra será parcelada em {}X de R$ {:.2f} e o TOTAL da compra ficará em R$ {:.2f}'.format(totalparcelas, parcela, totalfinal))
	elif opcao ==5:
		print('Fim do programa! ')
	else: 
		print('Opção inválida. Digite uma opçõa válida!')
print('Volte Sempre!')



# Biblioteca

# print('')
# print('{}'.format(''))
# = int(input(''))