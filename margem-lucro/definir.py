print("-"*23)
print("Definir Margem de Lucro")
print("-"*23)

custo_total = float(input("Digite o custo total: "))

margem_lucro = float(input("Digite a margem de lucro desejada %: "))

preco_venda = custo_total / (1 - margem_lucro)

print('O preço de venda: ', preco_venda)

lucro = preco_venda - custo_total

print('O lucro será de: ', lucro)