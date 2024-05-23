import pandas as pd

carros = pd.read_excel(io='carros.xlsx',)

for i, carro in carros.iterrows():
    marca = carro.get('marca')
    modelo = carro.get('modelo')
    ano = carro.get('ano')
    print(f'{maraca} - {modelo} - {ano}')