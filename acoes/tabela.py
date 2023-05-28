import requests
from chave import key
import pandas as pd
from io import StringIO
# from display import display

acao = "MXRF11.SA"

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={acao}&apikey={key}&datatype=csv'

r = requests.get(url)

print(r.text)

tabela = pd.read_csv(StringIO(r.text))
print(tabela)
# display(tabela)
