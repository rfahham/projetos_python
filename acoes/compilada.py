import requests
from colorama import Fore
from chave import key
import pandas as pd
from io import StringIO

acoes = ['PETR4.SAO', 'MXRF11.SA', 'VGIR11.SA', 'MCHF11.SA', 'VGIR11.SA']

compilada = pd.DataFrame()

for acao in acoes:
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={acao}&apikey={key}&datatype=csv'

    r = requests.get(url)

    tabela = pd.read_csv(StringIO(r.text))
    lista_tabelas = [compilada, tabela]
    compilada = pd.concat(lista_tabelas)
print(Fore.CYAN + "-" * 100)
print(compilada)
print(Fore.CYAN + "-" * 100)
print(Fore.WHITE + "")
