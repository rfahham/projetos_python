# pip install pathlib
# pip install pandas
# pip install openpyxl
# pip install pandera

import pandas as pd
from pandas import DataFrame
from pathlib import Path

# Caminho para o arquivo Excel
caminho_arquivo: Path = Path("../data/inventario_mundo.xlsx")

print(caminho_arquivo)

# Lendo o arquivo
df: DataFrame = pd.read_excel(caminho_arquivo)

print("--------------------------------")
print("Imprimindo as 5 primeiras linhas")
print("--------------------------------")
print(df.head())
print("")
print("-----------------------------------------------------------------")
print("Imprimindo produtos com quantidade acima de 5 unidades em estoque")
print("-----------------------------------------------------------------")
df_estoque_baixo: DataFrame = df[df["quantidade_estoque"] > 10]
print(df_estoque_baixo)
print("")
print("-------------------------------------------------------------------")
print("Imprimindo produtos com quantidade abaixo de 10 unidades em estoque")
print("-------------------------------------------------------------------")
disponiveis_e_baixo_estoque = df[(df["disponivel_venda"] == True) & (df["quantidade_estoque"] < 10)]
print(disponiveis_e_baixo_estoque)
print("")
print("-----------------------------------")
print("Calculando o valor total do estoque")
print("-----------------------------------")
df["valor_total_estoque"] = df["quantidade_estoque"] * df["preco_unitario"]
valor_total = df["valor_total_estoque"].sum()
print("Valor total em estoque:", valor_total)
print("")
print("------------------------------------")
print("Ordenando pela quantidade em estoque")
print("------------------------------------")
ordenado_por_preco = df.sort_values(by="preco_unitario", ascending=False)
print(ordenado_por_preco)
print("")
print("--------------------------")
print("Disponibilidade para venda")
print("--------------------------")
contagem_por_disponibilidade = df["disponivel_venda"].value_counts()
print(contagem_por_disponibilidade)
