#!/usr/bin/env python 
# -*- coding: utf-8 -*-

print('-_'*22)
print('Avaliando investimento')
print('-_'*22)
print('')

salario_bruto = 9500
salario_liquido = 6000
poupanca = 2000
saldo_poupanca = 100000
acoes = 1000
meses = 12
rendimento_poupanca = 0.06


salario_bruto_anual = salario_bruto * 12
salario_liquido_anual = salario_liquido * 12
poupanca_anual = poupanca * 12
acoes_anual = acoes * 12
total_aplicacoes = poupanca_anual + acoes_anual
total = saldo_poupanca + poupanca_anual + acoes_anual
rendimento_poupanca = (saldo_poupanca + poupanca_anual) + (saldo_poupanca + poupanca_anual) * 6

print("Salário Bruto Anual: ",  salario_bruto_anual)
print("Salário Líquido Anual: ", salario_liquido_anual)
print("Aplicação Poupança Anual: ", poupanca_anual)
print("Aplicação Açõoes Anual: ", acoes_anual)
print("Total Aplicacões Anual: ", total_aplicacoes)
print("Rendiemento Poupança: ", rendimento_poupanca)

print("Total Anual: ", total)
print("")