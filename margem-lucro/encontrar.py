print("-"*25)
print("Encontrar Margem de Lucro")
print("-"*25)

custo_total = float(input("Digite o valor do custo total: "))

preco_venda = float(input("Digite o valor de venda: "))

lucro = preco_venda - custo_total

# print(lucro)

margem = (lucro / preco_venda) * 100

# print(margem)

print('A margem foi de: ', margem, "%")