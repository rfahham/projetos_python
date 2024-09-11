# pip install pathlib
# pip install pandas
# pip install openpyxl

import pandas as pd
from pandas import DataFrame
# from pathlib import Path

minha_tabela: DataFrame = pd.read_excel("inventario_mundo.xlsx")

print(minha_tabela)