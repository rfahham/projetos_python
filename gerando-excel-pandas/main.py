# pip install pandas && openpyxl

import pandas as pd

carros = {
    'marca':['Fiat', 'Chevrolet', 'Ford'],
    'modelo':['Marea', 'Chevete', 'Escort'],
    'ano':['1999', '1978', '1995'],
}

dataframe = pd.DataFrame(carros)
dataframe.to_excel('./carros.xlsx')