from pathlib import Path

import pandas as pd
from pandas import DataFrame

from contrato_de_dados import InventarioDoMundoSchema

# Caminho para o arquivo Excel
caminho_arquivo: Path = Path("../data/inventario_mundo.xlsx")

print(caminho_arquivo)

# Lendo o arquivo
df: DataFrame = pd.read_excel(caminho_arquivo)

print("--------------------------------------------------------------------------------------------")
print("                                    Validar o DataFrame                                     ")
print("--------------------------------------------------------------------------------------------")
try:
    new_df = InventarioDoMundoSchema.validate(df)
    print(new_df)
    print("Validação bem-sucedida!")
except Exception as e:
    print(f"Erro de validação: {e}")